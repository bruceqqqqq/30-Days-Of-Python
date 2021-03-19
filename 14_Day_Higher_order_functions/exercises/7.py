countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
def upper_countries(country):
    return country.upper()

countries_upper = map(upper_countries, countries)
print(list(countries_upper))
