"""Test for user_table CRUD functions."""

import pytest

from app.db.base import create_db
from app.db.user_data import (
    NewUserData,
    UserData,
    create_user_data,
    delete_user_data,
    get_all_user_data,
    get_user_data,
    update_user_data,
)
from app.utils.random import create_random_string


def generate_random_user_data() -> UserData:
    rand_user_data = {
        "user_name": create_random_string(20),
        "user_password": create_random_string(20),
    }
    return NewUserData(**rand_user_data)


@pytest.mark.asyncio
async def test_create_user_data():
    db = await create_db()
    _create_user_data = generate_random_user_data()
    user_data = await create_user_data(db=db, new_user_data=_create_user_data)
    assert user_data.user_name == _create_user_data.user_name
    assert user_data.user_password == _create_user_data.user_password


@pytest.mark.asyncio
async def test_get_user_data():
    db = await create_db()
    user_data_in = generate_random_user_data()
    user_data_in_result = await create_user_data(db=db, new_user_data=user_data_in)
    user_data_out = await get_user_data(db=db, id=user_data_in_result.id)
    assert user_data_in.user_name == user_data_out.user_name
    assert user_data_in.user_password == user_data_out.user_password


@pytest.mark.asyncio
async def test_get_user_data_none_no_user():
    db = await create_db()
    assert not await get_user_data(db=db, id=42000000)


@pytest.mark.asyncio
async def test_get_10x_user_data():
    """Create and Read 10 user_data entries."""
    db = await create_db()
    for _ in range(5):
        user_data_in = generate_random_user_data()
        await create_user_data(db=db, new_user_data=user_data_in)
    user_data_lst = await get_all_user_data(db=db, offset=0, limit=10)
    for user_data in user_data_lst:
        assert isinstance(user_data.id, int)
        assert isinstance(user_data.user_name, str)
        assert isinstance(user_data.user_password, str)
        with pytest.raises(Exception):
            assert isinstance(user_data.id, str)


@pytest.mark.asyncio
async def test_update_user_data():
    db = await create_db()
    # Create user
    new_user = await create_user_data(
        db=db,
        new_user_data=generate_random_user_data(),
    )
    # Update result user data
    rand_pw = create_random_string(12)
    assert new_user.user_password != rand_pw
    new_user.user_password = rand_pw
    assert new_user.user_password == rand_pw
    # Execute user update query.
    err = await update_user_data(db=db, new_user_data=new_user)
    assert not isinstance(err, str)
    updated_user = await get_user_data(db=db, id=new_user.id)
    assert updated_user.user_password == rand_pw


@pytest.mark.asyncio
async def test_update_user_data_ensure_none_when_not_existing():
    db = await create_db()
    non_existing_user = UserData(
        **{"id": 4200000, "user_name": "John", "user_password": "Jane"}
    )
    assert not await update_user_data(db=db, new_user_data=non_existing_user)


@pytest.mark.asyncio
async def test_delete_user_data():
    db = await create_db()
    # Create user
    new_user = await create_user_data(
        db=db,
        new_user_data=generate_random_user_data(),
    )
    # Get user data
    _ = await get_user_data(db=db, id=new_user.id)
    # Delete user data
    await delete_user_data(db=db, id=new_user.id)
    # Get again, should thorugh an error
    assert not await get_user_data(db=db, id=new_user.id)
