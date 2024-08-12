from asynch.connection import Connection
from fastapi import Depends

from app.infrastructure.database.accessor import get_db_connection
from app.tasks.repository import TaskRepository
from app.tasks.service import TaskService


async def get_task_repository(
        conn: Connection = Depends(get_db_connection)
) -> TaskRepository:
    return TaskRepository(
        conn=conn
    )


async def get_task_service(
        task_repository: TaskRepository = Depends(get_task_repository)
) -> TaskService:
    return TaskService(
        task_repository=task_repository
    )
