from dataclasses import dataclass
from typing import List

from app.tasks.repository import TaskRepository
from app.tasks.schema import TaskSchema, TaskCreateSchema


@dataclass
class TaskService:
    task_repository: TaskRepository

    async def get_tasks(self) -> List[TaskSchema]:
        tasks = await self.task_repository.get_tasks()
        tasks_schema = [TaskSchema.model_validate(task) for task in tasks]
        return tasks_schema
