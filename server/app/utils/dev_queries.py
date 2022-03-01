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
    values_john = {"user_name": "John", "user_password": "John"}
    row = await database.execute(query=query, values=values_john)
    values_jane = {"user_name": "Jane", "user_password": "Jane"}
    row = await database.execute(query=query, values=values_jane)

    values = {"offset": 0, "limit": 10}
    query = """
        SELECT (id, user_name, user_password) FROM user_data
        ORDER BY id
        LIMIT :limit OFFSET :offset
    """
    rows = await database.fetch_all(query=query, values=values)
    for row in rows:
        logging.info(f"results: {row._row[0][0]}")


asyncio.run(main())
