"""Crud functions for todos table."""

from typing import List, Optional

from fastapi import HTTPException

from app.db.base import database
from app.db.models.models_generic import LimitOffset
from app.db.models.models_todo import NewTodo, Todo


async def create_todo(new_todo: NewTodo) -> Todo:
    query = """
        INSERT INTO todo (
            user_id,
            content_text,
            done
        ) VALUES (
            :user_id,
            :content_text,
            :done
        ) RETURNING (id, user_id, content_text, done);
    """
    values = new_todo.dict()
    try:
        row = await database.execute(query=query, values=values)
    except (Exception) as err:
        raise HTTPException(status_code=500, detail=f"err: {err}")
    todo = {"id": row[0], "user_id": row[1], "content_text": row[2], "done": row[3]}
    return Todo(**todo)


async def read_todo(todo_id: int) -> Optional[Todo]:
    query = "SELECT (id, user_id, content_text, done) FROM todo WHERE id = :id"
    row = await database.execute(query=query, values={"id": todo_id})
    if not row:
        return None
    data = {"id": row[0], "user_id": row[1], "content_text": row[2], "done": row[3]}
    return Todo(**data)


async def read_all_todo(limit_offset: LimitOffset) -> List[Todo]:
    query = """
        SELECT (id, user_id, content_text, done) FROM todo
        ORDER BY id
        LIMIT :limit OFFSET :offset
    """
    values = limit_offset.dict()
    records = await database.fetch_all(query=query, values=values)
    todos = []
    for record in records:
        row = record[0]
        data = {
            "id": row[0],
            "user_id": row[1],
            "content_text": row[2],
            "done": row[3],
        }
        todos.append(Todo(**data))
    return todos


async def update_todo(new_todo: Todo) -> Optional[Todo]:
    todo = await read_todo(todo_id=new_todo.id)
    if not todo:
        return None
    query = """
        UPDATE todo
        SET user_id = :user_id,
            content_text = :content_text,
            done = :done
        WHERE id = :id
        RETURNING (id, user_id, content_text, done);
    """
    row = await database.execute(query=query, values=new_todo.dict())
    data = {
        "id": row[0],
        "user_id": row[1],
        "content_text": row[2],
        "done": row[3],
    }
    return Todo(**data)


async def delete_todo_query(todo_id: int) -> None:
    query = """
        DELETE FROM todo
        WHERE id = :id;
    """
    await database.execute(query=query, values={"id": todo_id})
