names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']

def upper_names(name):
    return name.upper()

names_upper = map(upper_names, names)
print(list(names_upper))