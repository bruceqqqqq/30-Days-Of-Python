dog = {}
dog['name'] = 'Bruce'
dog['color'] = 'Black'
dog['Breed'] = 'Pitbull'
dog['Leg'] = 10.3
dog['Idade'] = '2 Years'

student = {
            'firstname': 'Diego', 'lastname': 'Fregolente', 'gender': 'Male',
            'marital status': 'Dating', 'country': 'Brazil', 'city': 'São Paulo',
            'address': {
                        'Street':'Estrada Agua Chata 3050', 'zip': '12345-321'
                       }
           }

lenght_student = len(student)

student['skills'] = ['HTML', 'Python']

print(type(student.get('skills')))
print(type(student.get('sasdasd')))

student['skills'].append('CSS')
print(student.get('skills'))

keys_dict = list(student.keys())
print(keys_dict)
values_dict = list(student.values())
print(values_dict)

listsdict = list(student.items())
print(listsdict)

student.popitem()
student.pop('firstname')
del student
