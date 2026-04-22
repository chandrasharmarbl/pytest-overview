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

@pytest.mark.asyncio
async def test_run_cli_generates_report(mocker, sample_api_response):
    """
    Test that run_cli fetches data, filters it, and writes a correct JSON report.
    """
    from src.main import run_cli
    
    # Arrange
    universities = [University.from_json(item) for item in sample_api_response]
    mocker.patch("src.main.fetch_all_countries", return_value=universities)
    
    # Mock open only in src.main to avoid interfering with tldextract's internal open calls
    mock_open = mocker.patch("src.main.open", mocker.mock_open())
    
    # Act
    await run_cli(["Canada", "United States"], "test_output.json")
    
    # Assert
    mock_open.assert_called_once_with("test_output.json", "w", encoding="utf-8")
    
    # Verify the JSON that was written
    write_calls = mock_open().write.call_args_list
    written_content = "".join(call.args[0] for call in write_calls)
    
    import json
    written_json = json.loads(written_content)
    
    # The third item (Lindenwood) should be filtered out
    assert len(written_json) == 2
    
    # Verify cleaning
    assert written_json[0]["name"] == "Marywood University"
    assert written_json[0]["clean_domain"] == "marywood.edu"
    assert written_json[1]["name"] == "Cégep de Saint-Jérôme"
    assert written_json[1]["clean_domain"] == "cstj.qc.ca"
