from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker

from app.settings import Settings

settings = Settings()

engine = create_async_engine(
    url=settings.db_url
)

AsyncSessionFactory = async_sessionmaker(
    engine,
    autocommit=False,
    expire_on_commit=False,
    class_=AsyncSession
)


async def get_db_session() -> AsyncSession:
    async with AsyncSessionFactory() as session:
        yield session
