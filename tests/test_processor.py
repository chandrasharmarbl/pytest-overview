import pytest
from src.processor import DomainUtils, Processor
from src.models import University

@pytest.mark.parametrize("input_url, expected_domain", [
    ("http://www.marywood.edu", "marywood.edu"),
    ("https://cstj.qc.ca", "cstj.qc.ca"),
    ("http://subdomain.example.com", "example.com"),
    ("https://www.ox.ac.uk", "ox.ac.uk"),
    ("http://localhost:8080", "localhost"),
    ("", ""),
    (None, ""),
])
def test_domain_cleaner(input_url, expected_domain):
    """
    Test that DomainUtils.clean correctly extracts the root domain from various URL formats.
    """
    assert DomainUtils.clean(input_url) == expected_domain

def test_filter_valid_universities(sample_api_response):
    """
    Test that Processor.filter_valid correctly removes universities 
    that have no web_pages.
    """
    # Arrange: Convert sample dictionaries to University objects
    universities = [University.from_json(item) for item in sample_api_response]
    
    # Our sample_api_response has 3 items, the 3rd one has `web_pages: []`
    
    # Act
    filtered = Processor.filter_valid(universities)
    
    # Assert
    assert len(filtered) == 2
    for uni in filtered:
        assert len(uni.web_pages) > 0
        assert uni.name != "Lindenwood University"
