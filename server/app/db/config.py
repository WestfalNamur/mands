from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine  # type: ignore
from sqlalchemy.orm import declarative_base, sessionmaker  # type: ignore

DATABASE_URL = "sqlite+aiosqlite:///./sqlite.db"

engine = create_async_engine(DATABASE_URL, future=True, echo=True)
async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
Base = declarative_base()
