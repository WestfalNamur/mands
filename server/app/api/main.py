"""Module to set up fastapi API to expose API to the outside world."""

from typing import Dict, Union

import databases
import uvicorn  # type: ignore
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

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

# Database
DATABASE_URL = (
    "postgresql+asyncpg://mands_user:mands_pw@localhost:5432/mands_db?sslmode=disable"
)
database = databases.Database(DATABASE_URL)


# Instantiate app and register routers.
app = FastAPI()


# For sanity check
@app.get("/ping")
def ping() -> Dict[str, str]:
    """Sanity test."""
    return {"msg": "pong"}


# lifecycle methodes
@app.on_event("startup")
async def startup() -> None:
    await database.connect()


@app.on_event("shutdown")
async def shutdown() -> None:
    await database.disconnect()


class NewUser(BaseModel):
    user_name: str
    user_password: str


class User(BaseModel):
    id: int
    user_name: str
    user_password: str


@app.post("/users")
async def create_user(new_user: NewUser) -> Union[str, User]:
    query = """
        INSERT INTO user_data (
            user_name,
            user_password
        ) VALUES (
            :user_name,
            :user_password
        ) RETURNING (id, user_name, user_password);
    """
    values = new_user.dict()
    try:
        row = await database.execute(query=query, values=values)
    except (Exception) as err:
        detail = f"err: {err}"
        raise HTTPException(status_code=409, detail=detail)
    user_data = {
        "id": row[0],
        "user_name": row[1],
        "user_password": row[2],
    }
    return User(**user_data)


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
