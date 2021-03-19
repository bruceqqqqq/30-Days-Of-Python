countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']

def morethansix(country):
    if len(country) >= 6:
        return True
    else:
        return False


countriessixormore = filter(morethansix, countries)
print(list(countriessixormore))