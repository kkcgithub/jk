import hashlib
import random

from PIL import Image, ImageDraw

from .base import ImageGenerator


class MockImageGenerator(ImageGenerator):
    """Generates placeholder art so the pipeline runs end-to-end without a
    paid image-generation API. The same prompt always produces the same
    image, so the noir post-process filter can be demoed/tested reliably.
    """

    def generate(self, prompt: str, size: tuple[int, int]) -> Image.Image:
        seed = int(hashlib.sha256(prompt.encode("utf-8")).hexdigest(), 16) % (2**32)
        rng = random.Random(seed)

        width, height = size
        image = Image.new("RGB", size, color=self._random_color(rng))
        draw = ImageDraw.Draw(image)

        for _ in range(rng.randint(5, 12)):
            shape_color = self._random_color(rng)
            x0, y0 = rng.randint(0, width), rng.randint(0, height)
            x1, y1 = rng.randint(0, width), rng.randint(0, height)
            bbox = [min(x0, x1), min(y0, y1), max(x0, x1), max(y0, y1)]
            if rng.random() < 0.5:
                draw.ellipse(bbox, fill=shape_color)
            else:
                draw.rectangle(bbox, fill=shape_color)

        return image

    @staticmethod
    def _random_color(rng: random.Random) -> tuple[int, int, int]:
        return (rng.randint(0, 255), rng.randint(0, 255), rng.randint(0, 255))
