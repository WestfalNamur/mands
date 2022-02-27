"""User models and user_data table CRUD functions.

note: User class represents a row in user_data.
"""

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
