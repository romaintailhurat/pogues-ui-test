from dataclasses import dataclass

@dataclass
class HomePage:
    """
    This class provides an API to the Pogues home page.
    """
    url: str = "https://pogues.dev.insee.io/"