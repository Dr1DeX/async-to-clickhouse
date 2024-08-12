from uuid import UUID

from pydantic import BaseModel


class TaskSchema(BaseModel):
    id: UUID
    name: str
    count: int


class TaskCreateSchema(BaseModel):
    name: str
    count: int
