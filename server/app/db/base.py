import os

import databases

mandsenv = os.environ["MANDSENV"]

# Database
DATABASE_URL = (
    "postgresql+asyncpg://mands_user:mands_pw@localhost:5432/mands_db?sslmode=disable"
)
if mandsenv == "testing":
    database = databases.Database(DATABASE_URL, force_rollback=True)
elif mandsenv == "dev":
    database = databases.Database(DATABASE_URL, force_rollback=False)
elif mandsenv == "production":
    database = databases.Database(DATABASE_URL, force_rollback=False)
else:
    database = databases.Database(DATABASE_URL, force_rollback=True)
