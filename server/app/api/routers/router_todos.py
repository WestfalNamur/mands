"""Router for /todos resource."""

from typing import Union

from fastapi import APIRouter

# from app.db.models.models_generic import LimitOffset
from app.db.models.models_todo import NewTodo, Todo
from app.db.queries.queries_todo import create_todo

router_todos: APIRouter = APIRouter()


@router_todos.post("/todos")
async def post_user(new_todo: NewTodo) -> Union[str, Todo]:
    return await create_todo(new_todo=new_todo)
