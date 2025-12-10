def city_country(city, country):
    """Return a string like 'Santiago, Chile'."""
    return f"{city.title()}, {country.title()}"

city = city_country('McKinney', 'USA')
print(city)

city = city_country('Paris', 'france')
print(city)

city = city_country('longyearbyen', 'svalbard')
print(city)
