person = {
    'name': 'Diego',
    'second_name': 'Fregolente',
    'age': 24,
    'country': 'Brasil',
    'is_married': False,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'addres': {
        'street': 'Rua são miguel dos campos, 50',
        'city': 'São Paulo'
    }
}

if len(person['skills']) > 0:
    print(f'Middle skills: {person["skills"][len(person["skills"])//2]}')
    if 'Python' in person['skills']:
        print(f'{person["name"]} has python in skills.')
    else:
        print(f'Diego don\'t have python in skills')
    if len(person['skills']) == 2 and 'JavaScript' in person['skills'] and 'React' in person['skills']:
        print('He is a front end developer')
    elif 'Node' in person['skills'] and 'Python' in person['skills'] and 'MongoDB' in person['skills']:
        if 'React' in person['skills']:
            print('He is a fullstack developer')
        else:
            print("He is a backend developer")
else:
    print(f'{person["name"]} has no skills')

if person['is_married'] and person['addres']['city'] == 'Finland':
    print(f'{person["name"]} {person["second_name"]} lives in {person["addres"]["city"]}. He is married')
