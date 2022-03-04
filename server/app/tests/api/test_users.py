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
        res = client.post(
            "/users",
            json=new_user,
        )
        assert res.status_code == 200
        assert isinstance(res.json()["id"], int)
        res = client.post(
            "/users",
            json=new_user,
        )
        assert res.status_code == 409
