ageInput = int(input('Enter your age: '))
if ageInput >= 18:
    print('You are old enough to drive.')
else:
    print(f'You need to wait {18 - ageInput} years to drive.')
