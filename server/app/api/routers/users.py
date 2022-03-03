"""Router for users resource."""

from fastapi import APIRouter

from app.db.base import create_db
from app.db.user_data import NewUserData, UserData, create_user_data

router_users: APIRouter = APIRouter()  # Mypy could not detect type otherwise.


# Depends?
@router_users.post("/users")
async def post_user(new_user_data: NewUserData) -> UserData:
    """Takes in username, and password and returns new user with id."""
    db = await create_db()
    user = await create_user_data(db=db, new_user_data=new_user_data)
    return user
