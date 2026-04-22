import asyncio
from typing import List
from src.client import ApiClient
from src.models import University

async def fetch_all_countries(countries: List[str]) -> List[University]:
    """
    Fetches universities for multiple countries concurrently.
    Flattens the results into a single list of University objects.
    """
    # Create a list of awaitable tasks for each country
    tasks = [ApiClient.fetch_universities(country) for country in countries]
    
    # Run them concurrently
    results = await asyncio.gather(*tasks)
    
    # `results` is a list of lists: [[Univ1, Univ2], [Univ3], ...]
    # We flatten it into a single list: [Univ1, Univ2, Univ3, ...]
    flattened_results = [uni for sublist in results for uni in sublist]
    return flattened_results
