from dataclasses import dataclass
from typing import List

from asynch.connection import Connection
from asynch.cursors import DictCursor

from app.tasks.models import Tasks


@dataclass
class TaskRepository:
    conn: Connection

    async def get_tasks(self) -> List[Tasks]:
        query = "SELECT * FROM Tasks"
        async with self.conn.cursor(cursor=DictCursor) as cursor:
            await cursor.execute(query=query)
            tasks = await cursor.fetchall()
            return tasks


