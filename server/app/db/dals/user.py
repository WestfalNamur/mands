from sqlalchemy.orm import Session  # type: ignore

from app.db.models.user import UserModel


class UserDAL:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    async def create_user(self, user_name: str, user_password: str) -> None:
        user_model = UserModel(user_name=user_name, user_password=user_password)
        self.db_session.add(user_model)
        await self.db_session.flush()
