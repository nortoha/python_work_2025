from city_functions import city_country

def test_city_country():
    """Does a simple city and country pair work?"""
    paris_france = city_country('paris', 'france')
    assert paris_france == 'Paris, France'