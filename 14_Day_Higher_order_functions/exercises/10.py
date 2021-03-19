countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']

def searchLand(country):
    if 'land' in country:
        return True
    else:
        return False

countries_with_land = filter(searchLand, countries)
print(list(countries_with_land))