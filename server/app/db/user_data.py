"""User models and user_data table CRUD functions.

note: User class represents a row in user_data.
"""

from typing import List

from pydantic import BaseModel
from databases import Database


# --------------------------------------------------------------------------------------
# Models
# --------------------------------------------------------------------------------------


class CreateUserData(BaseModel):
    user_name: str
    user_password: str


class UserData(BaseModel):
    id: int
    user_name: str
    user_password: str


# --------------------------------------------------------------------------------------
# CRUD
# --------------------------------------------------------------------------------------


async def create_user_data(db: Database, create_user_data: CreateUserData) -> UserData:
    """Query to add user to user_data table."""
    query = """
        INSERT INTO user_data (
            user_name,
            user_password
        ) VALUES (
            :user_name,
            :user_password
        ) RETURNING (id, user_name, user_password);
    """
    values = create_user_data.dict()
    row = await db.execute(query=query, values=values)
    user_data = {
        "id": row[0],
        "user_name": row[1],
        "user_password": row[2],
    }
    return UserData(**user_data)


async def get_user_data(db: Database, id: str) -> UserData:
    """Query to get single user_data by id."""
    query = "SELECT (id, user_name, user_password) FROM user_data WHERE id = :id"
    row = await db.execute(query=query, values={"id": id})
    user_data = {
        "id": row[0],
        "user_name": row[1],
        "user_password": row[2],
    }
    return UserData(**user_data)


async def get_all_user_data(db: Database, offset: int, limit: int) -> List[UserData]:
    """Query all data from user_table."""
    query = """
        SELECT (id, user_name, user_password) FROM user_data
        ORDER BY id
        LIMIT :limit OFFSET :offset
    """
    values = {"offset": offset, "limit": limit}
    rows = await db.fetch_all(query=query, values=values)
    lst_user_data = []
    for row in rows:
        # TODO: What exactly is returned?
        row = row[0]
        user_data = {
            "id": row[0],
            "user_name": row[1],
            "user_password": row[2],
        }
        lst_user_data.append(UserData(**user_data))
    return lst_user_data
