from dataclasses import dataclass
from typing import List, Optional, Dict, Any

@dataclass
class University:
    name: str
    country: str
    alpha_two_code: str
    domains: List[str]
    web_pages: List[str]
    state_province: Optional[str]

    @classmethod
    def from_json(cls, data: Dict[str, Any]) -> "University":
        """
        Creates a University instance from a JSON dictionary returned by HipoLabs API.
        Notice how 'state-province' from the API maps to 'state_province' in our model.
        """
        return cls(
            name=data.get("name", ""),
            country=data.get("country", ""),
            alpha_two_code=data.get("alpha_two_code", ""),
            domains=data.get("domains", []),
            web_pages=data.get("web_pages", []),
            state_province=data.get("state-province")
        )
