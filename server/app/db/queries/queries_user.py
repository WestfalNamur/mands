"""Crud functions for user_data table."""

from typing import List, Union

from fastapi import HTTPException

from app.db.base import database
from app.db.models.models_generic import LimitOffset
from app.db.models.models_user import NewUser, User


async def create_user(new_user: NewUser) -> User:
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
        raise HTTPException(status_code=500, detail=f"err: {err}")
    user_data = {
        "id": row[0],
        "user_name": row[1],
        "user_password": row[2],
    }
    return User(**user_data)


async def read_user(user_id: int) -> Union[User, None]:
    """Query to get single user_data by id."""
    query = "SELECT (id, user_name, user_password) FROM user_data WHERE id = :id"
    row = await database.execute(query=query, values={"id": user_id})
    if not row:
        return None
    user_data = {
        "id": row[0],
        "user_name": row[1],
        "user_password": row[2],
    }
    return User(**user_data)


async def read_all_user(limit_offset: LimitOffset) -> List[User]:
    """Query all data from user_table."""
    query = """
        SELECT (id, user_name, user_password) FROM user_data
        ORDER BY id
        LIMIT :limit OFFSET :offset
    """
    values = limit_offset.dict()
    records = await database.fetch_all(query=query, values=values)
    lst_user_data = []
    for record in records:
        row = record[0]
        user_data = {
            "id": row[0],
            "user_name": row[1],
            "user_password": row[2],
        }
        lst_user_data.append(User(**user_data))
    return lst_user_data


async def update_user_data(new_user_data: User) -> Union[User, None]:
    """Check if user exists and then update."""
    usr = await read_user(user_id=new_user_data.id)
    if not usr:
        return None
    query = """
        UPDATE user_data
        SET user_name = :user_name,
            user_password = :user_password
        WHERE id = :id
        RETURNING (id, user_name, user_password);
    """
    row = await database.execute(query=query, values=new_user_data.dict())
    updated_user_data = {
        "id": row[0],
        "user_name": row[1],
        "user_password": row[2],
    }
    return User(**updated_user_data)


async def delete_user_query(user_id: int) -> None:
    """Delete an existing user."""
    query = """
        DELETE FROM user_data
        WHERE id = :id;
    """
    await database.execute(query=query, values={"id": user_id})
