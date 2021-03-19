from functools import reduce

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']

def nice_place(coun):
    if coun == 'Sweden':
        return True
    else:
        return False

nice_country = filter(nice_place, countries)
print(list(nice_country))

names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']

def uppercase(name):
    return name.upper()

make_upper = map(uppercase, names)
print(list(make_upper))

numbers = [1, 2, 3, 4, 5]

def factorial(a, b):
    result = a * b
    return result


print(reduce(factorial, numbers))