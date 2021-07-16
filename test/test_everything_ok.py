from src.HomePage import HomePage

def test_ok():
    hp = HomePage()
    assert hp.url != "https://www.insee.fr"