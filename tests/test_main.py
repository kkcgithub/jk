from fastapi.testclient import TestClient

from noir_app.main import app

client = TestClient(app)


def test_index_page_loads():
    response = client.get("/")
    assert response.status_code == 200
    assert "Noir Painter" in response.text


def test_generate_returns_rendered_image():
    response = client.post("/generate", data={"description": "a rain-soaked alley"})
    assert response.status_code == 200
    assert "/generated/" in response.text


def test_generate_rejects_blank_description():
    response = client.post("/generate", data={"description": "   "})
    assert response.status_code == 200
    assert "must not be empty" in response.text
