from fastapi import FastAPI

from api.api_router import api_router

app = FastAPI()


@app.get("/")
def root():
    return {"msg": "Movies EDA API - Indicium Challenge"}


app.include_router(api_router)
