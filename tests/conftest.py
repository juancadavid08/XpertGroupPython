import pytest
from unittest.mock import AsyncMock, MagicMock
from app.services import user_service
from bson import ObjectId
from app.utils.security import hash_password


@pytest.fixture(autouse=True)
def mock_db(monkeypatch):
    fake_db = MagicMock()
    fake_users = MagicMock()

    # almacenamiento simulado en memoria
    inserted_users = {}

    async def find_one_mock(query):
        return inserted_users.get(query.get("username"))

    async def insert_one_mock(user):
        user["_id"] = ObjectId()
        inserted_users[user["username"]] = user
        return {"inserted_id": user["_id"]}

    fake_cursor = MagicMock()
    fake_cursor.to_list = AsyncMock(return_value=list(inserted_users.values()))

    fake_users.find = MagicMock(return_value=fake_cursor)
    fake_users.find_one = AsyncMock(side_effect=find_one_mock)
    fake_users.insert_one = AsyncMock(side_effect=insert_one_mock)

    fake_db.__getitem__.return_value = fake_users
    monkeypatch.setattr(user_service, "db", fake_db)