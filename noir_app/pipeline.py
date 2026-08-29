import uuid
from pathlib import Path

from . import config
from .generation.factory import get_generator
from .noir.filter import apply_noir_filter
from .noir.prompt import build_noir_prompt


def render_noir_image(description: str) -> Path:
    """End-to-end: description -> noir prompt -> generated image -> noir
    post-process -> saved PNG. Returns the path of the saved file.
    """
    prompt = build_noir_prompt(description)
    generator = get_generator(config.IMAGE_GEN_PROVIDER)
    image = generator.generate(prompt, config.IMAGE_SIZE)
    styled = apply_noir_filter(image)

    filename = f"{uuid.uuid4().hex}.png"
    output_path = config.GENERATED_DIR / filename
    styled.save(output_path)
    return output_path
