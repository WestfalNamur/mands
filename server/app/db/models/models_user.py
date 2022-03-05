"""Pydantic models for user_data."""

from pydantic import BaseModel


class BaseUser(BaseModel):
    user_name: str
    user_password: str


class NewUser(BaseUser):
    pass


class User(BaseUser):
    id: int
