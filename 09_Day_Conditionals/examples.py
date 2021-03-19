# if example

a = 3

if a == 3:
    print('A equal to 3')

if a > 0:
    print('A is a positive number')

if a < 0:
    print('A is a negative number')
else:
    print('A is a positive number')

if a > 0:
    print('A is a positive number')
elif a < 0:
    print('A is a negative number')
else:
    print('A equal to zero')

print('A is positive') if a > 0 else print('A is negative')
