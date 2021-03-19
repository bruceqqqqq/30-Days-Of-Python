fruits = ['banana', 'orange', 'mango', 'lemon']
fruit = str(input('Enter a fruit: ')).strip().lower()
if fruit not in fruits:
    fruits.append(fruit)
    print(fruits)
else:
    print(f'{fruit} already in the list')
