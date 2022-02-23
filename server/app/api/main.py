"""Module to setup fastapi API to expose API to the outside world."""

from typing import Dict

from fastapi import FastAPI
import uvicorn  # type: ignore


app = FastAPI()


@app.get("/ping")
def ping() -> Dict[str, str]:
    """Sanity test."""
    return {"msg": "Success!"}


def run(host: str, port: int) -> None:
    """Run the API."""
    uvicorn.run(app, host=host, port=port)
