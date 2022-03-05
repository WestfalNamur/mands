"""Pydantic models for todos."""

from pydantic import BaseModel


class BaseTodo(BaseModel):
    user_id: int
    content_text: str
    done: bool


class NewTodo(BaseTodo):
    pass


class Todo(BaseTodo):
    id: int
