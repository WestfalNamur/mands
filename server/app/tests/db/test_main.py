"""Test if our db connection setup is correct, and we can interact with the db."""

import pytest
import asyncio
from databases import Database

from app.db.base import DB_SOURCE

@pytest.mark.asyncio
async def test_main():
    # Create db
    database = Database(DB_SOURCE, force_rollback=True)
    await database.connect()
    # Create a table and drop table.
    query_drop_table = """DROP TABLE IF EXISTS high_score"""
    query_create_table = """CREATE TABLE high_score (id INTEGER PRIMARY KEY, name VARCHAR(100), score INTEGER)"""
    await database.execute(query=query_drop_table)
    await database.execute(query=query_create_table)
    await database.execute(query=query_drop_table)


