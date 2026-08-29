from noir_app import config
from noir_app.pipeline import render_noir_image


def test_render_noir_image_creates_a_png(tmp_path, monkeypatch):
    monkeypatch.setattr(config, "GENERATED_DIR", tmp_path)
    monkeypatch.setattr(config, "IMAGE_SIZE", (32, 32))

    output_path = render_noir_image("a lonely street at midnight")

    assert output_path.exists()
    assert output_path.suffix == ".png"
    assert output_path.parent == tmp_path
