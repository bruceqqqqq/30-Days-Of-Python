countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']

def lensix(country):
    if len(country) == 6:
        return True
    else:
        return False

countrieswithsixcharacteres = filter(lensix, countries)
print(list(countrieswithsixcharacteres))