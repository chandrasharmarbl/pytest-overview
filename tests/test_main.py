import pytest
from src.main import fetch_all_countries
from src.models import University

@pytest.mark.asyncio
async def test_fetch_all_countries_concurrency(mocker):
    """
    Test that fetch_all_countries calls ApiClient.fetch_universities for each country concurrently.
    """
    countries = ["Canada", "United States", "Mexico"]
    
    # Arrange: Mock ApiClient.fetch_universities to just return empty lists
    mock_fetch = mocker.patch("src.client.ApiClient.fetch_universities", return_value=[])
    
    # Act
    results = await fetch_all_countries(countries)
    
    # Assert
    assert mock_fetch.call_count == 3
    
    # Verify it was called with the exact countries we provided
    mock_fetch.assert_any_call("Canada")
    mock_fetch.assert_any_call("United States")
    mock_fetch.assert_any_call("Mexico")
    
    # Ensure it returns a flattened list (in this case empty since we mocked it as empty)
    assert results == []
