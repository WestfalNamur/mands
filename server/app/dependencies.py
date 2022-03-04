from typing import Any, AsyncGenerator

from app.db.config import async_session
from app.db.dals.user import UserDAL


async def get_user_dal() -> AsyncGenerator[UserDAL, Any]:
    async with async_session() as session:
        async with session.begin():
            yield UserDAL(session)
