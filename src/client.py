import httpx
from typing import List
from src.models import University

class ApiError(Exception):
    """Custom exception for API errors."""
    pass

class ApiClient:
    BASE_URL = "http://universities.hipolabs.com/search"

    @classmethod
    async def fetch_universities(cls, country: str) -> List[University]:
        """
        Fetches universities for a given country asynchronously.
        """
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(cls.BASE_URL, params={"country": country})
                response.raise_for_status()
                data = response.json()
                return [University.from_json(item) for item in data]
        except httpx.HTTPError as e:
            raise ApiError(str(e)) from e
