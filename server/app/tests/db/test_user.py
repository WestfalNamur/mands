"""Test for user_table CRUD functions."""

import pytest

from app.tests.db.test_base import create_test_db
from app.db.user_data import create_user_data, CreateUserData
from app.utils.random import create_random_string


@pytest.mark.asyncio
async def test_create_user_data():
    db = await create_test_db()
    _create_user_data = CreateUserData(
        **{
            "user_name": create_random_string(21),
            "user_password": create_random_string(21),
        }
    )
    user_data = await create_user_data(db=db, create_user_data=_create_user_data)
    assert user_data.user_name == _create_user_data.user_name
    assert user_data.user_password == _create_user_data.user_password
