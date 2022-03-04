from fastapi.testclient import TestClient

from app.api.main import app
from app.utils.random_data_generator import create_random_string


def test_users_post() -> None:
    with TestClient(app) as client:
        """
        post /users should:
            1. return 200
            2. json with user_name, user_password, and id
            3. return 400 when username duplicated.
        """
        new_user = {
            "user_name": create_random_string(20),
            "user_password": create_random_string(20),
        }
        res = client.post("/users", json=new_user)
        assert res.status_code == 200
        assert isinstance(res.json()["id"], int)
        res = client.post("/users", json=new_user)
        assert res.status_code == 500


def test_users_get() -> None:
    with TestClient(app) as client:
        """
        get /users/id should:
            1. return 200 + user data if ther is a user.
            2. return 200 + None if user does not exist.
        """
        res = client.get("/users/9000")
        assert res.status_code == 200
        assert res.json() is None
        new_user = {
            "user_name": create_random_string(20),
            "user_password": create_random_string(20),
        }
        res = client.post("/users", json=new_user)
        assert res.status_code == 200
        user_id = res.json()["id"]
        res = client.get(f"/users/{user_id}")
        assert res.status_code == 200
        assert res.json()["user_name"] == new_user["user_name"]
        assert res.json()["user_password"] == new_user["user_password"]


def test_users_get_all() -> None:
    with TestClient(app) as client:
        """
        get /users should:
            1. return 200 + List of users
            2. return 200 + Empty list if no user in db.
            3. return
        """
        for _ in range(5):
            new_user = {
                "user_name": create_random_string(20),
                "user_password": create_random_string(20),
            }
            res = client.post("/users", json=new_user)
            assert res.status_code == 200

        res = client.get("/users", json={"limit": 100, "offset": 0})
        assert res.status_code == 200
        assert len(res.json()) >= 5
        res = client.get("/users", json={"offset": 0})
        assert res.status_code == 422


def test_user_put() -> None:
    with TestClient(app) as client:
        """
        get /users should:
            1. return 200 + List of users
            2. return 200 + Empty list if no user in db.
            3. return
        """
        user_v1 = {
            "user_name": create_random_string(20),
            "user_password": create_random_string(20),
        }
        res = client.post("/users", json=user_v1)
        user_v2 = res.json()
        user_v2["user_password"] = create_random_string(20)
        assert res.status_code == 200
        res = client.put("/users", json=user_v2)
        data = res.json()
        assert res.status_code == 200
        assert data["user_name"] == user_v1["user_name"]
        assert data["user_password"] != user_v1["user_password"]
        assert data["user_name"] == user_v2["user_name"]
        assert data["user_password"] == user_v2["user_password"]
        user_v3 = data
        user_v3["id"] = 42000
        res = client.put("/users", json=user_v3)
        assert res.status_code == 200
        assert res.json() is None


def test_users_delete():
    with TestClient(app) as client:
        """
        get /users should:
            1. return 200 + List of users
            2. return 200 + Empty list if no user in db.
            3. return
        """
        user = {
            "user_name": create_random_string(20),
            "user_password": create_random_string(20),
        }
        res = client.post("/users", json=user)
        assert res.status_code == 200
        user_id = res.json()["id"]
        res = client.get(f"/users/{user_id}")
        assert res.status_code == 200
        assert res.json()["user_name"] == user["user_name"]
        res = client.delete(f"/users/{user_id}")
        assert res.status_code == 200
        res = client.get(f"/users/{user_id}")
        assert res.status_code == 200
        assert res.json() is None
