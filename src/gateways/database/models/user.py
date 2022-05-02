from sqlalchemy import Boolean, Column, DateTime, Integer, String
from sqlalchemy.orm import declarative_base  # type:ignore[attr-defined]
from sqlalchemy.sql import func

Base = declarative_base()


class TelegramUser(Base):
    __tablename__ = "tg_user"
    pk = Column(Integer, primary_key=True)
    id = Column(Integer)
    is_bot = Column(Boolean)
    first_name = Column(String)
    last_name = Column(String)
    username = Column(String)
    language_code = Column(String)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())
