"""User models and user_data table CRUD functions.

note: User class represents a row in user_data.
"""

from typing import List, Union

from databases import Database
from pydantic import BaseModel

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


async def get_user_data(db: Database, id: int) -> Union[UserData, None]:
    """Query to get single user_data by id."""
    query = "SELECT (id, user_name, user_password) FROM user_data WHERE id = :id"
    row = await db.execute(query=query, values={"id": id})
    if not row:
        return None
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
    records = await db.fetch_all(query=query, values=values)
    lst_user_data = []
    for record in records:
        row = record[0]
        user_data = {
            "id": row[0],
            "user_name": row[1],
            "user_password": row[2],
        }
        lst_user_data.append(UserData(**user_data))
    return lst_user_data


async def update_user_data(
    db: Database, new_user_data: UserData
) -> Union[UserData, None]:
    """Check if user exists and then update."""
    usr = await get_user_data(db=db, id=new_user_data.id)
    if not usr:
        return None
    query = """
        UPDATE user_data
        SET user_name = :user_name,
            user_password = :user_password
        WHERE id = :id
        RETURNING (id, user_name, user_password);
    """
    row = await db.execute(query=query, values=new_user_data.dict())
    updated_user_data = {
        "id": row[0],
        "user_name": row[1],
        "user_password": row[2],
    }
    return UserData(**updated_user_data)


async def delete_user_data(db: Database, id: int) -> None:
    """Delete an existing user."""
    query = """DELETE FROM user_data WHERE id = :id;"""
    await db.execute(query=query, values={"id": id})
