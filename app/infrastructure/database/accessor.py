from asynch import connect
from asynch.connection import Connection

from app.settings import Settings

settings = Settings()


async def get_db_connection() -> Connection:
    conn = await connect(
        host=settings.DB_HOST,
        port=settings.DB_PORT,
        database=settings.DB_NAME,
        user=settings.DB_USER,
        password=settings.DB_PASSWORD
    )
    return conn
