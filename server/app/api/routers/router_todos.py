"""Router for /todos resource."""

from typing import List, Union

from fastapi import APIRouter

from app.db.models.models_generic import LimitOffset
from app.db.models.models_todo import NewTodo, Todo
from app.db.queries.queries_todo import (
    create_todo,
    delete_todo_query,
    read_all_todo,
    read_todo,
    update_todo,
)

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


@router_todos.put("/todos")
async def put_todo(new_todo: Todo) -> Union[Todo, None]:
    return await update_todo(new_todo=new_todo)


@router_todos.delete("/todos/{todo_id}")
async def delete_todo(todo_id: int) -> None:
    return await delete_todo_query(todo_id=todo_id)
