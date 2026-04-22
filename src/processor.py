import tldextract
from typing import List
from src.models import University

class DomainUtils:
    @staticmethod
    def clean(url: str) -> str:
        """
        Extracts the root domain from a given URL.
        Handles http, https, www, subdomains, and localhost.
        Returns an empty string for invalid or empty inputs.
        """
        if not url:
            return ""
        
        extracted = tldextract.extract(url)
        
        if extracted.suffix:
            return f"{extracted.domain}.{extracted.suffix}"
        
        # Fallback for things like 'localhost'
        return extracted.domain

class Processor:
    @staticmethod
    def filter_valid(universities: List[University]) -> List[University]:
        """
        Filters out universities that have no web_pages.
        """
        return [uni for uni in universities if uni.web_pages]
