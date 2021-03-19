yourAge = int(input('Enter your age: '))
myAge = 25
differenceAge = yourAge - myAge
if yourAge > myAge:
    if differenceAge == 1:
        print(f'Bro you its just a 1 year more old than me.')
    elif differenceAge > 1:
        print(f'You are {differenceAge} years more old than me')
elif differenceAge == 0:
    print(f'We have the same age bro!')
else:
    print(f'I am {abs(differenceAge)} more old than you, haha.')
