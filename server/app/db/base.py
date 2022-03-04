import databases

# Database
DATABASE_URL = (
    "postgresql+asyncpg://mands_user:mands_pw@localhost:5432/mands_db?sslmode=disable"
)
database = databases.Database(DATABASE_URL)
