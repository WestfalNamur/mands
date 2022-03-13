"""Router for /users resource."""

from typing import List, Optional, Union

from fastapi import APIRouter

from app.db.models.models_generic import LimitOffset
from app.db.models.models_user import NewUser, User
from app.db.queries.queries_user import (
    create_user,
    delete_user_query,
    read_all_user,
    read_user,
    update_user_data,
)

router_users: APIRouter = APIRouter()


@router_users.post("/users")
async def post_user(new_user: NewUser) -> Union[str, User]:
    return await create_user(new_user=new_user)


@router_users.get("/users/{user_id}")
async def get_user(user_id: int) -> Optional[User]:
    return await read_user(user_id=user_id)


@router_users.get("/users")
async def get_all_user(limit_offset: LimitOffset) -> List[User]:
    return await read_all_user(limit_offset=limit_offset)


@router_users.put("/users")
async def put_user(new_data: User) -> Optional[User]:
    return await update_user_data(new_user_data=new_data)


@router_users.delete("/users/{user_id}")
async def delete_user(user_id: int) -> None:
    return await delete_user_query(user_id=user_id)
