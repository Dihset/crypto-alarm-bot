from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from ..models.user import TelegramUser


async def get_or_create_user(session: AsyncSession, user) -> TelegramUser:
    qs = select(TelegramUser).where(TelegramUser.id == user.id)
    execution = await session.execute(qs)
    db_user = execution.fetchone()
    if not db_user:
        db_user = TelegramUser(
            id=user.id,
            is_bot=user.is_bot,
            first_name=user.first_name,
            last_name=user.last_name,
            username=user.username,
            language_code=user.language_code,
        )
        session.add(db_user)
        await session.commit()
    return db_user
