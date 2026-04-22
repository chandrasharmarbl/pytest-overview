import tldextract

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
