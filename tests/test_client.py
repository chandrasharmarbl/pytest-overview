import pytest
import httpx
from src.client import ApiClient, ApiError

@pytest.mark.asyncio
async def test_fetch_universities_success(mocker, sample_api_response):
    """
    Test that fetch_universities makes a GET request and returns a list of University objects.
    We mock the network call to avoid hitting the actual API.
    """
    mock_response = mocker.Mock()
    mock_response.status_code = 200
    
    # Filter the mock response to simulate what the real API would return for Canada
    canadian_data = [u for u in sample_api_response if u["country"] == "Canada"]
    mock_response.json.return_value = canadian_data
    
    mock_get = mocker.patch("httpx.AsyncClient.get", return_value=mock_response)
    
    universities = await ApiClient.fetch_universities("Canada")
    
    assert len(universities) == 1
    assert universities[0].name == "Cégep de Saint-Jérôme"
    assert universities[0].country == "Canada"
    
    mock_get.assert_called_once_with("http://universities.hipolabs.com/search", params={"country": "Canada"})

@pytest.mark.asyncio
async def test_fetch_universities_error_handling(mocker):
    """
    Test that an httpx.HTTPError is caught and raised as our custom ApiError.
    """
    # Arrange: mock httpx.AsyncClient.get to raise an exception
    mocker.patch("httpx.AsyncClient.get", side_effect=httpx.HTTPError("Mocked timeout or 404"))
    
    # Act & Assert
    with pytest.raises(ApiError) as exc_info:
        await ApiClient.fetch_universities("Canada")
    
    assert "Mocked timeout or 404" in str(exc_info.value)
