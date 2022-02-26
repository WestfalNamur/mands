"""Base for our async database connection.

    engine: https://www.encode.io/databases/
    testing: https://www.encode.io/databases/tests_and_migrations/
    FastAPI: https://fastapi.tiangolo.com/advanced/async-sql-databases/?h=sql
"""

from databases import Database

DB_SOURCE = "postgresql://mands_user:mands_pw@localhost:5432/mands_db?sslmode=disable"


async def create_db(db_source_url: str, testing=False) -> Database:
    """Create a db conneciton."""
    if testing:
        database = Database(db_source_url, force_rollback=True)
    else:
        database = Database(db_source_url, force_rollback=False)
    await database.connect()
    return database

