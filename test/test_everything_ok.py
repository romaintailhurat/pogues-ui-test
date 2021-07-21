"""
The main goal of this file is to make sure that the test infra
is ok.
"""
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

def test_ok(suite_browser):
    hp = HomePage(browser = suite_browser)
    assert hp.url != "https://www.insee.fr"