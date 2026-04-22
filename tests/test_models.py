from src.models import University
import pytest

def test_university_creation_from_json(sample_api_response):
    """
    Test that we can instantiate a University object using the 'from_json'
    class method, using a dictionary from our sample API response.
    """
    # Arrange: Grab the first university from our sample data
    university_data = sample_api_response[0]
    
    # Act: Attempt to create the object
    university = University.from_json(university_data)
    
    # Assert: Verify the attributes match the input data
    assert university.name == "Marywood University"
    assert university.country == "United States"
    assert university.alpha_two_code == "US"
    assert university.domains == ["marywood.edu"]
    assert university.web_pages == ["http://www.marywood.edu"]
    assert university.state_province is None
