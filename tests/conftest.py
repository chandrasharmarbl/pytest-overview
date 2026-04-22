import pytest

@pytest.fixture
def sample_api_response():
    """
    A sample JSON response matching the structure of HipoLabs University Domains and Names API.
    """
    return [
        {
            "domains": ["marywood.edu"],
            "web_pages": ["http://www.marywood.edu"],
            "state-province": None,
            "name": "Marywood University",
            "country": "United States",
            "alpha_two_code": "US"
        },
        {
            "domains": ["cstj.qc.ca"],
            "web_pages": ["https://www.cstj.qc.ca", "https://cstj.qc.ca"],
            "state-province": "Quebec",
            "name": "Cégep de Saint-Jérôme",
            "country": "Canada",
            "alpha_two_code": "CA"
        },
        {
            "domains": ["lindenwood.edu"],
            "web_pages": [],  # Intentionally empty for testing our filtering
            "state-province": "Missouri",
            "name": "Lindenwood University",
            "country": "United States",
            "alpha_two_code": "US"
        }
    ]
