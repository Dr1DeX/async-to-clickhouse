import asyncio
from logging.config import fileConfig

from alembic import context
from sqlalchemy.ext.asyncio import create_async_engine

from app.infrastructure.database import Base
from app.settings import Settings


config = context.config

if config.config_file_name is not None:
    fileConfig(config.config_file_name)

target_metadata = Base.metadata


def do_migrations_offline(connection) -> None:

    context.configure(
        connection=connection,
        target_metadata=target_metadata,
        # literal_binds=True,
        include_schemas=True,
        compare_type=True

    )

    with context.begin_transaction():
        context.run_migrations()


async def run_migrations_online() -> None:

    connectable = create_async_engine(url=Settings().db_url, future=True)

    async with connectable.connect() as connection:
        await connection.run_sync(do_migrations_offline)


asyncio.run(run_migrations_online())
