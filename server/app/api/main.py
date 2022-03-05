"""Module to set up fastapi API to expose API to the outside world."""

from typing import Dict

import uvicorn  # type: ignore
from fastapi import FastAPI

from app.api.routers.router_todos import router_todos
from app.api.routers.router_users import router_users
from app.db.base import database

# --------------------------------------------------------------------------------------
# Setup
#
# Create FastAPI instance which will be our app run as a single process run by our
# server program Uvicorn. We can run multiple server programs to make use of multiple
# cores on our machine. For more infos see the FastAPI documentation.
# https://fastapi.tiangolo.com/deployment/server-workers/?h=gunicorn
# --------------------------------------------------------------------------------------


# Instantiate app and register routers.
app = FastAPI()
app.include_router(router_users)
app.include_router(router_todos)


# A dummy for route for sanity checks.
@app.get("/ping")
def ping() -> Dict[str, str]:
    """Sanity test."""
    return {"msg": "pong"}


# app lifecycle methods.
@app.on_event("startup")
async def startup() -> None:
    await database.connect()


@app.on_event("shutdown")
async def shutdown() -> None:
    await database.disconnect()


# ------------------------------------------------------------------------------
# Run
#
# uvicorn:
#   Uvicorn is a process manager. Gunicorn is a server program in a single process.
#   Together Uvicorn acts a process manager that manages one or more Gunicorn
#   process that run out app.
# ------------------------------------------------------------------------------


def run(host: str, port: int) -> None:
    """Run the API."""
    uvicorn.run(app, host=host, port=port)
