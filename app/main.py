from fastapi import FastAPI
from app.api.cats import router as cats_router
from app.api.users import router as user_router

app = FastAPI()

app.include_router(cats_router, prefix="/cats")
app.include_router(user_router, prefix="/users")