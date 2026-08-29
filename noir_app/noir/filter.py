import numpy as np
from PIL import Image, ImageEnhance, ImageOps


def apply_noir_filter(
    image: Image.Image,
    *,
    desaturation: float = 0.85,
    contrast: float = 1.4,
    grain_strength: float = 18,
    vignette_strength: float = 0.6,
    seed: int | None = None,
) -> Image.Image:
    """Push any source image toward a consistent noir look, independent of
    how the underlying generator rendered it: desaturate, boost contrast,
    darken the edges, and add film grain.
    """
    image = image.convert("RGB")
    image = _desaturate(image, desaturation)
    image = ImageEnhance.Contrast(image).enhance(contrast)
    image = _apply_vignette(image, vignette_strength)
    image = _apply_grain(image, grain_strength, seed)
    return image


def _desaturate(image: Image.Image, amount: float) -> Image.Image:
    grayscale = ImageOps.grayscale(image).convert("RGB")
    return Image.blend(image, grayscale, amount)


def _apply_vignette(image: Image.Image, strength: float) -> Image.Image:
    if strength <= 0:
        return image

    width, height = image.size
    y, x = np.ogrid[:height, :width]
    center_x, center_y = width / 2, height / 2
    max_dist = np.sqrt(center_x**2 + center_y**2)
    dist = np.sqrt((x - center_x) ** 2 + (y - center_y) ** 2) / max_dist
    darkening = 1 - strength * np.clip(dist, 0, 1) ** 2

    array = np.asarray(image).astype(np.float32)
    array *= darkening[..., None]
    return Image.fromarray(np.clip(array, 0, 255).astype(np.uint8))


def _apply_grain(image: Image.Image, strength: float, seed: int | None) -> Image.Image:
    if strength <= 0:
        return image

    rng = np.random.default_rng(seed)
    array = np.asarray(image).astype(np.int16)
    noise = rng.normal(0, strength, array.shape[:2])
    array += noise[..., None].astype(np.int16)
    return Image.fromarray(np.clip(array, 0, 255).astype(np.uint8))
