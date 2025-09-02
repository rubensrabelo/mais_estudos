from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

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
