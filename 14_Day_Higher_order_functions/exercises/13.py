countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']

def startwithE(country: str) -> bool:
    if country.startswith('E'):
        return True
    else:
        return False

countrieswithstartE = filter(startwithE, countries)
print(list(countrieswithstartE))
