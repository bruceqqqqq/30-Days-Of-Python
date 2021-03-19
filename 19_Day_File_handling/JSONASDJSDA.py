import json

# person_json = '''{
#     "name": "Diego",
#     "country": "Brazil",
#     "city": "São Paulo",
#     "skills": ["Python"]
# }'''
#
# person_dict = json.loads(person_json)
# print(person_dict['name'])
# print(person_dict)

person = {
    'name': 'Diego',
    'country': 'Brazil',
    'skills': ['Python']
}

person1 = {
    'name': 'Diego',
    'country': 'Brazil',
    'skills': ['Python']
}
# person_json = json.dumps(person, indent=4) # indent can be 2, 4, 8
# print(type(person_json)) # because of triple quotes
# print(person_json)


with open('json_example.json', 'w') as file:
    json.dump(person, file, ensure_ascii=False, indent=4)
    json.dump(person1, file, ensure_ascii=False, indent=4)