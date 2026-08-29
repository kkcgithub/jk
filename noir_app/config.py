import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
GENERATED_DIR = BASE_DIR / "generated"
GENERATED_DIR.mkdir(exist_ok=True)

IMAGE_GEN_PROVIDER = os.environ.get("IMAGE_GEN_PROVIDER", "mock")
IMAGE_SIZE = (768, 768)
