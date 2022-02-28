"""Test for user_table CRUD functions."""

import pytest

from app.tests.db.test_base import create_test_db
from app.db.user_data import (
    UserData,
    create_user_data,
    CreateUserData,
    get_all_user_data,
    get_user_data,
)
from app.utils.random import create_random_string


def generate_random_user_data() -> UserData:
    rand_user_data = {
        "user_name": create_random_string(21),
        "user_password": create_random_string(21),
    }
    return CreateUserData(**rand_user_data)


@pytest.mark.asyncio
async def test_create_user_data():
    db = await create_test_db()
    _create_user_data = generate_random_user_data()
    user_data = await create_user_data(db=db, create_user_data=_create_user_data)
    assert user_data.user_name == _create_user_data.user_name
    assert user_data.user_password == _create_user_data.user_password


@pytest.mark.asyncio
async def test_get_user_data():
    db = await create_test_db()
    user_data_in = generate_random_user_data()
    user_data_in_result = await create_user_data(db=db, create_user_data=user_data_in)
    user_data_out = await get_user_data(db=db, id=user_data_in_result.id)
    assert user_data_in.user_name == user_data_out.user_name
    assert user_data_in.user_password == user_data_out.user_password


@pytest.mark.asyncio
async def test_get_user_data():
    """Create and Read 5 user_data entries."""
    db = await create_test_db()
    for _ in range(5):
        user_data_in = generate_random_user_data()
        await create_user_data(db=db, create_user_data=user_data_in)
    user_data_lst = await get_all_user_data(db=db, offset=0, limit=10)
    # for user_data in user_data_lst:
    #     assert isinstance(user_data.id, int)
    #     assert isinstance(user_data.user_name, str)
    #     assert isinstance(user_data.user_password, str)
    #     with pytest.raises(Exception):
    #         assert isinstance(user_data.id, str)
