empty_dict = {}
empty_dict = dict()

dct = {'Name': 'Diego', 'Second Name': 'Fregolente', 'Age': 24}

person = {
    'name': 'Diego',
    'last_name': 'Biagi',
    'age': 24,
    'country': 'Brazil',
    'is_married': False,
    'skills': ['Trying Python', 'Gaming'],
    'adress': { 'City': 'São Paulo',
                'Street': 'R. S Miguel dos Campos',
}
}


print(len(person))

print(person['name'])
print(person['skills'])
print(person['adress']['City'])
print(person.get('city')) # if the key does not exist "get" will return a None, instead of error
person['skills'].append('Pycharm')
person['height'] = 120

print(person['height'])
print(person['skills'])

person['last_name'] = 'Fregolente'

print('name' in person)

dct.pop('Name')
dct.popitem()
del dct['Second Name']
print(dct)

print(person.items())

# person.clear() this remove all data in dict

person_copy = person.copy() # this make a copy of dict if you make like person_copy = person will create a relation

print(person_copy.keys())
print(person_copy.values())


