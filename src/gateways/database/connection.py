"""Base database setup and connection."""
from sqlalchemy.ext.asyncio.engine import create_async_engine
from sqlalchemy.ext.asyncio.session import AsyncSession
from sqlalchemy.orm.session import sessionmaker as _sessionmaker
from sqlalchemy.pool import NullPool

from src.core.config import settings

engine = create_async_engine(settings.SQLALCHEMY_PG_URI, poolclass=NullPool)
sessionmaker = _sessionmaker(bind=engine, class_=AsyncSession)
