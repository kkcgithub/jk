from .base import ImageGenerator
from .mock import MockImageGenerator


def get_generator(provider: str) -> ImageGenerator:
    if provider == "mock":
        return MockImageGenerator()
    raise NotImplementedError(
        f"Image generation provider '{provider}' is not implemented yet. "
        "Add an ImageGenerator subclass in noir_app/generation/ and "
        "register it here."
    )
