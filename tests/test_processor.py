import pytest
from src.processor import DomainUtils

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
