from fastapi import FastAPI
from user_task.core.config import settings
from user_task.api.api.api import api_router

app = FastAPI(title=settings.PROJECT_NAME)
app.include_router(api_router)

