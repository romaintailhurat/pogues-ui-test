from dataclasses import dataclass
from typing import Any

@dataclass
class HomePage:
    """
    This class provides an API to the Pogues home page.
    """
    browser: Any
    url: str = "https://pogues.dev.insee.io/"

    def get_title(self):
        return self.browser.title