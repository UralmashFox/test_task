from fastapi import APIRouter
from user_task.api.api.endpoints import users

api_router = APIRouter()
api_router.include_router(users.router, prefix="/users", tags=['Users'])
