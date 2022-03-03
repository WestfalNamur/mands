"""Base for our async database connection.

    engine: https://www.encode.io/databases/
    testing: https://www.encode.io/databases/tests_and_migrations/
    FastAPI: https://fastapi.tiangolo.com/advanced/async-sql-databases/?h=sql
"""
import os

from databases import Database

DB_SOURCE = "postgresql://mands_user:mands_pw@localhost:5432/mands_db?sslmode=disable"


async def create_db() -> Database:
    """Create a db connection pool."""
    mands_env = os.environ["MANDSENV"]
    force_rollback = False if mands_env == "testing" else True
    database = Database(DB_SOURCE, force_rollback=force_rollback)
    await database.connect()
    return database
