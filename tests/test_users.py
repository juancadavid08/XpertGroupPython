import pytest
from httpx import AsyncClient, ASGITransport
from app.main import app
import uuid
import asyncio

if asyncio.get_event_loop().is_closed():
    asyncio.set_event_loop(asyncio.new_event_loop())


@pytest.mark.asyncio
async def test_create_user():
    transport = ASGITransport(app=app)
    unique = str(uuid.uuid4())[:8]
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        response = await ac.post("/users/", json={
            "first_name": "Test",
            "last_name": unique,
            "password": "secret123"
        })
    print(response.status_code, response.json())
    assert response.status_code == 200
    assert "username" in response.json()

@pytest.mark.asyncio
async def test_login_user():
    transport = ASGITransport(app=app)
    unique = str(uuid.uuid4())[:8]
    first_name = "Test"
    last_name = unique
    password = "secret123"
    expected_username = f"{first_name.lower()}.{last_name.lower()}"

    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        # Crear usuario
        response = await ac.post("/users/", json={
            "first_name": first_name,
            "last_name": last_name,
            "password": password
        })
        assert response.status_code == 200
        assert response.json()["username"] == expected_username

        # Login con username generado
        response = await ac.post("/users/login", json={
            "username": expected_username,
            "password": password
        })
        print(response.status_code, response.json())  # <-- útil para depurar
        assert response.status_code == 200


@pytest.mark.asyncio
async def test_get_users():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        response = await ac.get("/users/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)