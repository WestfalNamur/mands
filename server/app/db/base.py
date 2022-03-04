import os

import databases

mandsenv = os.environ["MANDSENV"]

DATABASE_URL = (
    "postgresql+asyncpg://mands_user:mands_pw@localhost:5432/mands_db?sslmode=disable"
)

if mandsenv in ["dev", "production"]:
    database = databases.Database(DATABASE_URL, force_rollback=False)
else:
    database = databases.Database(DATABASE_URL, force_rollback=True)
