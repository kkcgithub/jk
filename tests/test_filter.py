from PIL import Image

from noir_app.noir.filter import apply_noir_filter


def test_apply_noir_filter_preserves_size_and_mode():
    image = Image.new("RGB", (64, 64), color=(200, 50, 50))
    result = apply_noir_filter(image, seed=1)
    assert result.size == (64, 64)
    assert result.mode == "RGB"


def test_apply_noir_filter_desaturates_fully_when_requested():
    image = Image.new("RGB", (64, 64), color=(255, 0, 0))
    result = apply_noir_filter(
        image,
        desaturation=1.0,
        contrast=1.0,
        grain_strength=0,
        vignette_strength=0,
        seed=1,
    )
    r, g, b = result.getpixel((32, 32))
    assert abs(r - g) < 5
    assert abs(g - b) < 5


def test_apply_noir_filter_vignette_darkens_corners_more_than_center():
    image = Image.new("RGB", (64, 64), color=(200, 200, 200))
    result = apply_noir_filter(
        image,
        desaturation=0,
        contrast=1.0,
        grain_strength=0,
        vignette_strength=0.8,
        seed=1,
    )
    center = sum(result.getpixel((32, 32)))
    corner = sum(result.getpixel((0, 0)))
    assert corner < center
