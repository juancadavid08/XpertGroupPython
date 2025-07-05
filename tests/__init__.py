import pytest
from httpx import AsyncClient
from app.main import app

@pytest.mark.asyncio
async def test_create_user():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/users/", json={
            "first_name": "Test",
            "last_name": "User",
            "password": "secret123"
        })
    assert response.status_code == 200
    assert "username" in response.json()

@pytest.mark.asyncio
async def test_login_user():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        # Este usuario debe haber sido creado previamente
        response = await ac.post("/users/login", json={
            "username": "test.user",
            "password": "secret123"
        })
    assert response.status_code == 200
    assert "username" in response.json()

@pytest.mark.asyncio
async def test_get_users():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/users/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)