from fastapi.testclient import TestClient

from app.api.main import app
from app.utils.random_data_generator import create_random_string


def test_todos_create() -> None:
    with TestClient(app) as client:
        """
        post /todos should:
            1. return 200
            2. return JSON of Todo schema.
            3. Fail if user does not exist
        """
        # Creat user to add todos to.
        user = {
            "user_name": create_random_string(20),
            "user_password": create_random_string(20),
        }
        res = client.post("/users", json=user)
        assert res.status_code == 200
        user_id = res.json()["id"]
        # Add new_todo
        new_todo = {
            "user_id": user_id,
            "content_text": create_random_string(20),
            "done": False,
        }
        res = client.post("/todos", json=new_todo)
        assert res.status_code == 200
        assert isinstance(res.json()["id"], int)
        # Add new_todo to non-existing user.
        new_todo["user_id"] = 42000
        res = client.post("/todos", json=new_todo)
        assert res.status_code == 500
