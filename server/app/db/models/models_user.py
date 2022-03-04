from pydantic import BaseModel


class NewUser(BaseModel):
    user_name: str
    user_password: str


class User(BaseModel):
    id: int
    user_name: str
    user_password: str
