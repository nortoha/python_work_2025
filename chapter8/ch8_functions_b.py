#def  make_shirt(size, message):
#    """Ex8-3 Display information about the shirt."""
#    print(f"You ordered a {size} shirt with the following text printed on it:")
#    print(message)

def  make_shirt(size='large', message='I love Python'):
    """Ex8-4 Display information about the shirt."""
    print(f"You ordered a {size} shirt with the following text printed on it:")
    print(message)

def describe_city(city_name, country='USA'):
    """Ex8-5 Print a sentence about the city"""
    print(f"{city_name} is in {country}")

## Ex 8-3
#call using positional arguments
make_shirt("medium", "I turn coffee into code.") 

#call using keyword arguments
make_shirt(size='large', message='Count your blessings.')
make_shirt(message='Count your blessings.', size='large')

## Ex 8-4
make_shirt(size='medium')    
make_shirt(message='I love Java.')

## Ex 8-5
describe_city('McKinney')
describe_city('Paris', 'France')
describe_city(city_name='Rome', country='Italy')