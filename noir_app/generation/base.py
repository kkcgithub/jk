from abc import ABC, abstractmethod

from PIL import Image


class ImageGenerator(ABC):
    """Interface every image-generation backend must implement.

    Swapping the mock generator for a real provider (OpenAI, Stability AI,
    etc.) means adding a subclass here and registering it in factory.py --
    nothing in noir_app.pipeline needs to change.
    """

    @abstractmethod
    def generate(self, prompt: str, size: tuple[int, int]) -> Image.Image:
        raise NotImplementedError
