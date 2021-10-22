list_names = ['Los Angels', 'Busan', 'London', 'New York', 'Paris']

# write from start
with open('cities.txt', 'w') as cities_file:
    for city in list_names:
        print(city, file=cities_file)
    print('=' * 20, file=cities_file)

# append update
with open('places.txt', 'a') as places_file:
    for place in list_names:
        print(place, file=places_file)
    print('=' * 20, file=places_file)

# create if not exist
try:
    with open('places.txt', 'x') as places_file:
        for place in list_names:
            print(place, file=places_file)
        print('=' * 20, file=places_file)
    if places_file is BaseException():
        raise places_file

except BaseException as err:
    print('ERROR: ', err)
