"""Module to set up fastapi API to expose API to the outside world."""

from typing import Dict

import uvicorn  # type: ignore
from fastapi import FastAPI

from app.api.routers.users import router_users
from app.db.config import Base, engine

# ------------------------------------------------------------------------------
# Setup
#
# Create FastAPI instance which will be our app run as a single process run by our
# server program Uvicorn. We can run multiple server programs to make use of multiple
# cores on our machine. For more infos see the FastAPI documentation.
# https://fastapi.tiangolo.com/deployment/server-workers/?h=gunicorn
# Register routers in app.
#
# Create a database connection pool.
# ------------------------------------------------------------------------------


# Instantiate app and register routers.
app = FastAPI()
app.include_router(router_users)


@app.on_event("startup")
async def startup() -> None:
    # create db tables
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


# ------------------------------------------------------------------------------
# Run
#
# uvicorn:
#   Uvicorn is a process manager. Gunicorn is a server program in a single process.
#   Together Uvicorn acts a process manager that manages one or more Gunicorn
#   process that run out app.
# ------------------------------------------------------------------------------

# For sanity check
@app.get("/ping")
def ping() -> Dict[str, str]:
    """Sanity test."""
    return {"msg": "pong"}


def run(host: str, port: int) -> None:
    """Run the API."""
    uvicorn.run(app, host=host, port=port)
