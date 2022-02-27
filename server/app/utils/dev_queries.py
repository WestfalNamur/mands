"""Template to play with queries."""

import asyncio
import logging
from databases import Database

from app.db.base import DB_SOURCE

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

database = Database(DB_SOURCE, force_rollback=True)


async def main() -> None:

    await database.connect()

    values = {
        "user_name": "rand_name",
        "user_password": "rand_pw",
    }
    query = """
        INSERT INTO user_data (
            user_name,
            user_password
        ) VALUES (
            :user_name,
            :user_password
        ) RETURNING (id, user_name, user_password);
    """
    row = await database.execute(query=query, values=values)
    results = {
        "id": row[0],
        "user_name": row[1],
        "user_password": row[2],
    }
    logging.info(f"results: {results}")


asyncio.run(main())
