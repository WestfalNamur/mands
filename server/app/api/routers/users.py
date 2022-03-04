from fastapi import APIRouter, Depends

from app.db.dals.user import UserDAL
from app.dependencies import get_user_dal

router_users = APIRouter()


@router_users.post("/users")
async def create_user(
    user_name: str, user_password: str, user_dal: UserDAL = Depends(get_user_dal)
) -> None:
    return await user_dal.create_user(user_name=user_name, user_password=user_password)
