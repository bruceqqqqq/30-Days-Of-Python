def sum_of_five(a, b, c, d, e):
    return a + b + c + d + e

lst = [1, 2, 3, 4, 5]
print(sum_of_five(*lst)) # * for tuple/list ** for dict

numbers = range(2, 7)
print(list(numbers))  # another way of unpacking

countries = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']
fin, sw, nor, *rest = countries
print(rest)

numbers = [1, 2, 3, 4, 5, 6, 7]
one, *middle, last = numbers

print(middle, one, last)

def unpacking_person_info(name, country, city, age):
    return f'{name} lives in {country}, {city}. He is {age} year old.'

dct = {'name':'Asabeneh', 'country':'Finland', 'city':'Helsinki', 'age':250}
print(unpacking_person_info(**dct))
print(unpacking_person_info(*dct))

def sum_all(*args): # we use this for list or
    s = 0
    for i in args:
        s += i
    return s

print(sum_all(1, 2, 3))
print(sum_all(3, 9))

def packingpersoninfo(**kwargs):
    for key in kwargs:
        print(f'{key} = {kwargs[key]}')
    return kwargs

myinfodict = (packingpersoninfo(name='Diego', country='Brasil', age=24))

print(myinfodict)
print(type(myinfodict))

