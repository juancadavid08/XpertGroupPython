from fastapi import HTTPException
from app.models.schemas import User, Login
from app.db.mongo import db
from app.utils.security import hash_password, verify_password

class UserService:
    async def get_users(self):
        users = await db["users"].find().to_list(100)
        for u in users:
            u["id"] = str(u.pop("_id"))
            u.pop("password", None)
        return users

    async def create_user(self, user: User):
        username = f"{user.first_name.lower()}.{user.last_name.lower()}"
        exists = await db["users"].find_one({"username": username})
        if exists:
            raise HTTPException(400, "Username already exists")
        user_dict = user.model_dump()
        user_dict["username"] = username
        user_dict["password"] = hash_password(user.password)
        await db["users"].insert_one(user_dict)
        return {"message": "User created", "username": username}

    async def login(self, data: Login):
        user = await db["users"].find_one({"username": data.username})
        if not user or not verify_password(data.password, user["password"]):
            raise HTTPException(401, "Invalid credentials")
        user.pop("password", None)
        user["id"] = str(user.pop("_id"))
        return user