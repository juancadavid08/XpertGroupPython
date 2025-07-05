from motor.motor_asyncio import AsyncIOMotorClient

client = AsyncIOMotorClient("mongodb://host.docker.internal:27017")
db = client["cat_api_db"]