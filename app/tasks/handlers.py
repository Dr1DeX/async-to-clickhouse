from typing import List, Annotated

from fastapi import APIRouter, Depends

from app.tasks.schema import TaskSchema
from app.tasks.service import TaskService
from dependency import get_task_service

router = APIRouter(prefix='/tasks', tags=['tasks'])


@router.get(
    '',
    response_model=List[TaskSchema]
)
async def get_tasks(
        task_service: Annotated[TaskService, Depends(get_task_service)]
):
    return await task_service.get_tasks()
