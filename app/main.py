from fastapi import FastAPI

from app.tasks.handlers import router as task_router

app = FastAPI(title='mega app')

app.include_router(task_router)
