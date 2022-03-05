"""Router for /todos resource."""

from typing import List, Union

from fastapi import APIRouter

from app.db.models.models_generic import LimitOffset
from app.db.models.models_todo import NewTodo, Todo
from app.db.queries.queries_todo import create_todo, read_all_todo, read_todo

router_todos: APIRouter = APIRouter()


@router_todos.post("/todos")
async def post_todo(new_todo: NewTodo) -> Union[str, Todo]:
    return await create_todo(new_todo=new_todo)


@router_todos.get("/todos/{todo_id}")
async def get_todo(todo_id: int) -> Union[Todo, None]:
    return await read_todo(todo_id=todo_id)


@router_todos.get("/todos")
async def get_all_todo(limit_offset: LimitOffset) -> List[Todo]:
    return await read_all_todo(limit_offset=limit_offset)
