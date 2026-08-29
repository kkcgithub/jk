from pathlib import Path

from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from . import config
from .pipeline import render_noir_image

BASE_DIR = Path(__file__).resolve().parent

app = FastAPI(title="Noir Painter")
app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")
app.mount("/generated", StaticFiles(directory=config.GENERATED_DIR), name="generated")
templates = Jinja2Templates(directory=BASE_DIR / "templates")


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse(
        request,
        "index.html",
        {"image_url": None, "description": "", "error": None},
    )


@app.post("/generate", response_class=HTMLResponse)
async def generate(request: Request, description: str = Form(...)):
    try:
        output_path = render_noir_image(description)
        image_url = f"/generated/{output_path.name}"
        error = None
    except ValueError as exc:
        image_url = None
        error = str(exc)

    return templates.TemplateResponse(
        request,
        "index.html",
        {
            "image_url": image_url,
            "description": description,
            "error": error,
        },
    )
