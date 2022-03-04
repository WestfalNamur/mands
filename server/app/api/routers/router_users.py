from typing import Union

from fastapi import APIRouter

from app.db.models.models_user import NewUser, User
from app.db.queries.queries_user import create_user

router_users: APIRouter = APIRouter()


@router_users.post("/users")
async def post_user(new_user: NewUser) -> Union[str, User]:
    return await create_user(new_user=new_user)
