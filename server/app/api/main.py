"""Module to setup fastapi API to expose API to the outside world."""

from typing import Dict

from fastapi import FastAPI
import uvicorn  # type: ignore


# Create FastAPI instane which will be our app run as a single process run by our
# server program Uvicorn. We can run multiple server programs to make use of multiple
# cores on our machine. For more infos see the FastAPI documention.
# https://fastapi.tiangolo.com/deployment/server-workers/?h=gunicorn
app = FastAPI()


@app.get("/ping")
def ping() -> Dict[str, str]:
    """Sanity test."""
    return {"msg": "pong"}


def run(host: str, port: int) -> None:
    """Run the API.

    uvicorn:
        Uvicorn is a process manager. Gunicorn is a server program in a single process.
        Together Uvicorn acts a process manager that manages one or more Gunicorn
        process that run out app.
    """
    uvicorn.run(app, host=host, port=port)
