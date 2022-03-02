"""Template to play with queries."""

import asyncio
import logging

from databases import Database

DB_SOURCE = "postgresql://mands_user:mands_pw@localhost:5432/mands_db?sslmode=disable"

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

database = Database(DB_SOURCE, force_rollback=True)


async def main() -> None:

    await database.connect()

    query = """
        INSERT INTO user_data (
            user_name,
            user_password
        ) VALUES (
            :user_name,
            :user_password
        ) RETURNING (id, user_name, user_password);
    """
    values = {"user_name": "John", "user_password": "John"}
    row_create = await database.execute(query=query, values=values)

    query = """
        UPDATE user_data
        SET user_name = :user_name,
            user_password = :user_password
        WHERE id = :id
        RETURNING (id, user_name, user_password);
    """
    values = {
        "id": row_create[0],
        "user_name": row_create[1],
        "user_password": "42",
    }
    try:
        row_update = await database.execute(query=query, values=values)
    except Exception as err:
        print(f"error: {err}")
    print(row_update)


asyncio.run(main())
