"""Crud functions for todos table."""

# from typing import List, Union

from fastapi import HTTPException

from app.db.base import database

# from app.db.models.models_generic import LimitOffset
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
