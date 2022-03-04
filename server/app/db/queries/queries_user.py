from fastapi import HTTPException

from app.db.base import database
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
