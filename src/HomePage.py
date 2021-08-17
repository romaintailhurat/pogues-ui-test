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

    def get_questionnaires_list(self):
        questionnaires_list_elements = self.browser.find_by_css(".question-list-item-name > a")
        names = [qle.text for qle in questionnaires_list_elements]        
        return names
