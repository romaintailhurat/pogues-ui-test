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
        names = [element.text for element in questionnaires_list_elements]        
        return names

    def search_questionnaire(self, name: str):
        name = name.lower() # FIXME search using uppercase letters doesn't work ?!
        search_input = self.browser.find_by_css("#questionnaire-list .ctrl-input input")
        search_input.fill(name)
        return self.get_questionnaires_list()

    def create_questionnaire(self, name = "ui-test-questionnaire", id = "UI_TEST_QUESTIONNAIRE"):
        # TODO waiting for the test application to be debugged =(
        pass

    
