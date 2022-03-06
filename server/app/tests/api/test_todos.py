from typing import List

from fastapi.testclient import TestClient
from pydantic import parse_obj_as

from app.api.main import app
from app.db.models.models_todo import Todo
from app.utils.random_data_generator import create_random_string


def create_user(client: TestClient) -> int:
    user = {
        "user_name": create_random_string(20),
        "user_password": create_random_string(20),
    }
    res = client.post("/users", json=user)
    assert res.status_code == 200
    user_id = res.json()["id"]
    return user_id


def create_todo(client: TestClient, user_id: int) -> Todo:
    new_todo = {
        "user_id": user_id,
        "content_text": create_random_string(20),
        "done": False,
    }
    res = client.post("/todos", json=new_todo)
    assert res.status_code == 200
    return Todo(**res.json())


def test_todos_create() -> None:
    with TestClient(app) as client:
        """
        post /todos should:
            1. return 200
            2. return JSON of Todo schema.
            3. Fail if user does not exist
        """
        user_id = create_user(client=client)
        _ = create_todo(client=client, user_id=user_id)
        # Add new_todo to non-existing user.
        new_todo = {
            "user_id": 42000,
            "content_text": create_random_string(20),
            "done": False,
        }
        res = client.post("/todos", json=new_todo)
        assert res.status_code == 500


def test_todos_get() -> None:
    with TestClient(app) as client:
        """
        get /todos/{todo_id} should:
            1. return 200 and todo or none.
        """
        user_id = create_user(client=client)
        todo = create_todo(client=client, user_id=user_id)
        res = client.get(f"/todos/{todo.id}")
        assert res.status_code == 200
        assert Todo(**res.json())
        res = client.get("/todos/42000")
        assert res.status_code == 200
        assert res.json() is None


def test_todos_get_all() -> None:
    with TestClient(app) as client:
        """
        get /todos should:
            1. return 200 and todos or [].
        """
        user_id = create_user(client=client)
        for _ in range(5):
            create_todo(client=client, user_id=user_id)
        res = client.get("/todos/?limit=5&offset=0")
        assert res.status_code == 200
        assert parse_obj_as(List[Todo], res.json())


def test_todos_put():
    with TestClient(app) as client:
        """
        put /todos should:
            return 200 & None if not existing
            return 200 & updated version of the todo
        """
        user_id = create_user(client=client)
        todo_original = create_todo(client=client, user_id=user_id)
        todo_original.done = True
        res = client.put("/todos", json=todo_original.dict())
        assert res.status_code == 200
        assert Todo(**res.json())
        todo_updated = client.get(f"/todos/{todo_original.id}")
        assert todo_updated.status_code == 200
        assert todo_updated.json()["done"]


def test_todo_delete():
    with TestClient(app) as client:
        """
        delete /todos should:
            return 200 & None
        """
        user_id = create_user(client=client)
        todo = create_todo(client=client, user_id=user_id)
        res = client.get(f"/todos/{todo.id}")
        assert res.status_code == 200
        assert Todo(**res.json())
        res = client.delete(f"/todos/{todo.id}")
        assert res.status_code == 200
        res = client.get(f"/todos/{todo.id}")
        assert res.status_code == 200
        assert res.json() is None
