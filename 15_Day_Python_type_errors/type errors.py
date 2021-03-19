# print 'hello world' Missing parentheses in call to 'print'. Did you mean print('hello world')? - Syntax Error

try:
    print(a)
except Exception as error: # a is not defined yet
    print(error, type(error))

numbers = [1, 2, 3]
try:
    print(numbers[3]) # numbers as no index 3 because 0 1 2
except Exception as error:
    print(error, type(error))

try:
    import maths # maths doesn't exist
except Exception as error:
    print(error, type(error))

try:
    import math
    print(math.PI) # the right way to verify "pi" its with math.pi (lower_case)
except Exception as error:
    print(error, type(error))

users = {'name':'Diego', 'age':24, 'country':'Brazil'}
try:
    print(users['county']) # thats a mistake, you forgot 'R' in word country
except Exception as error:
    print(error, type(error))

try:
    3 + '4' # Impossible to concatenated or sum INT with STR values
except Exception as error:
    print(error, type(error))

try:
    3 + int('4') # Now have no error, because we convert str('4') for int('4')
except Exception as error:
    print(error, type(error))

try:
    print(int('Tres')) # cannot convert because letters cannot convert to int with base 10:
except Exception as error:
    print(error, type(error))

try:
    from math import power # this will not work because in math power receive name of pow
except Exception as error:
    print(error, type(error))

try:
    1 / 0 # Its impossible to divide a number by zero
except Exception as error:
    print(error, type(error))
