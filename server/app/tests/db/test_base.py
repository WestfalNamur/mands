"""Test if our db connection setup is correct, and we can interact with the db."""

import pytest

from app.db.base import DB_SOURCE, create_db


async def create_test_db():
    return await create_db(db_source_url=DB_SOURCE, testing=True)


@pytest.mark.asyncio
async def test_main():
    """Check out db connection.

    1. Await connection
    2. Create table high_score. This should work otherwise a previous test run did not
    roll back the changes.
    3. Now we try to create the table a 2nd time within this test, and it should fail.
    4. As we run in testing mode all should be rolled back later.

    """
    # Create db
    database = await create_test_db()
    # Create a table and drop table.
    query_create_table = """
        CREATE TABLE high_score (
            id INTEGER PRIMARY KEY,
            name VARCHAR(100
        ), score INTEGER)
    """
    await database.execute(query=query_create_table)
    with pytest.raises(Exception):
        await database.execute(query=query_create_table)
