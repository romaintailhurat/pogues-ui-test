from splinter import Browser
from selenium import webdriver
import pytest
from src.HomePage import HomePage

@pytest.fixture
def suite_browser():
    # Setting up Chrome Options in order to have it run in a container
    opts = webdriver.ChromeOptions()
    opts.add_argument("--headless")
    opts.add_argument("--no-sandbox")
    opts.add_argument("--disable-gpu")
    opts.add_argument("--disable-extensions")
    browser = Browser("chrome", options=opts)

    return browser

def test_title_is_ok(suite_browser):
    hp = HomePage(browser = suite_browser)
    hp.browser.visit(hp.url)    
    assert hp.get_title() == "Pogues"

def test_questionnaires_list_search_displays_the_right_item(suite_browser):
    # FIXME code a real case
    hp = HomePage(browser = suite_browser)
    hp.browser.visit(hp.url)
    questionnaires_list = hp.get_questionnaires_list()
    first_questionnaire = questionnaires_list[0]
    list_after_search = hp.search_questionnaire(first_questionnaire)
    assert len(list_after_search) == 1 and list_after_search[0] == first_questionnaire
