"""Tests for users resource."""

from app.tests.api.test_main import client
from app.utils.random import create_random_string


def test_post_new_user():
    new_user = {
        "user_name": create_random_string(12),
        "user_password": create_random_string(12),
    }
    res = client.post("/users", json=new_user)
    assert res.status_code == 200
    assert isinstance(res.json()["id"], int)
