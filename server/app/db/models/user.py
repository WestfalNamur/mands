from sqlalchemy import Column, Integer, String  # type: ignore

from app.db.config import Base


class UserModel(Base):  # type: ignore
    __tablename__ = "user_data"

    id = Column(Integer, primary_key=True)
    user_name = Column(String, nullable=False, unique=True)
    user_password = Column(String, nullable=False)
