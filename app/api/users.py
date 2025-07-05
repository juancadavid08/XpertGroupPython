from fastapi import APIRouter, HTTPException
from app.models.schemas import User, Login
from app.services.user_service import UserService

router = APIRouter()
user_service = UserService()

@router.get("/")
async def get_users():
    return await user_service.get_users()

@router.post("/")
async def create_user(user: User):
    return await user_service.create_user(user)

@router.post("/login")
async def login(data: Login):
    return await user_service.login(data)