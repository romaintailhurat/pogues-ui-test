"""
The main goal of this file is to make sure that the test infra
is ok.
"""
from src.HomePage import HomePage

def test_ok():
    hp = HomePage()
    assert hp.url != "https://www.insee.fr"