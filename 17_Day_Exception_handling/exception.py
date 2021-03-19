# try:
#     print(10 + '5')
# except:
#     print('Something went wrong')
#

try:
    name = input('Name:')
    year_born = input('Year Born:') # need to be int to fix type error
    age = 2021 - int(year_born)
    print(f'You are {name} and your age is {age}.')
except TypeError:
    print('Type Error, verify your variables')
except ValueError:
    print('Value Error, verify your variables')
except ZeroDivisionError:
    print('Dont divide by zero, are you stupid?') # except need to have error to run

else: # if have no errors run with try
    print('I usually run with the try block')
finally: # if or not found a error, will run
    print('I always will run')