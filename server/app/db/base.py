"""Base for our database connection.

We init the database object which is used to run queries against out Postgres db.
The database is configured here and connects to Postgres on the "startup" lifecycle
event of the app (see. app/app/main.py). The database objet can then be used to run
queries. All queries run via one connection.
"""

import os

import databases

mandsenv = os.environ["MANDSENV"]
DATABASE_URL = os.environ["DATABASE_URL"]

# Set asyncpg driver to allow concurrent requests to Postgres.
DATABASE_URL_ASYNC = DATABASE_URL.replace("postgresql", "postgresql+asyncpg")

if mandsenv in ["dev", "production"]:
    database = databases.Database(DATABASE_URL_ASYNC, force_rollback=False)
else:
    database = databases.Database(DATABASE_URL_ASYNC, force_rollback=True)
