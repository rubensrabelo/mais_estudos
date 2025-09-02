from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pathlib import Path
import os

from api.api_router import api_router

app = FastAPI()


@app.get("/", response_model=dict)
def root() -> dict:
    return {"msg": "Movies EDA API - Indicium Challenge"}


app.include_router(api_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


BASE_DIR = Path(__file__).resolve().parent  # pasta onde main.py está
IMG_DIR = BASE_DIR / "img"
IMG_DIR.mkdir(parents=True, exist_ok=True)

# Serve a mesma pasta onde os plots serão salvos
app.mount("/img", StaticFiles(directory=IMG_DIR), name="img")