from fastapi import APIRouter, HTTPException
import httpx

router = APIRouter()

API_KEY = "live_JBT0Ah0Nt12iyl2IpjQVLDWjcLk0GQwf4zI9wBMfmfejKmcC31mOJp4yJz5TsOUP"
BASE_URL = "https://api.thecatapi.com/v1"
headers = {"x-api-key": API_KEY}

@router.get("/breeds")
async def get_breeds():
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{BASE_URL}/breeds", headers=headers)
        return response.json()

@router.get("/breeds/{breed_id}")
async def get_breed_by_id(breed_id: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{BASE_URL}/breeds/{breed_id}", headers=headers)
        if response.status_code == 404:
            raise HTTPException(404, "Breed not found")
        if response.status_code != 200:
            raise HTTPException(response.status_code, f"Error from API: {response.text}")
        return response.json()

@router.get("/breeds/search")
async def search_breeds(q: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{BASE_URL}/breeds/search?q={q}", headers=headers)
        return response.json()