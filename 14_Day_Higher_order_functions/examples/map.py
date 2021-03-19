# map function

numbers = [1, 2, 3, 4, 5]

def squares(x):
    return x ** 2

numbers_squared_x = map(squares, numbers) # map take function and iterable by parameters POGCHAMP :O
# print(list(numbers_squared))

# Now with lambda function

numbers_squared = map(lambda x : x ** 2, numbers ) # pogchamp
print(list(numbers_squared))

numbers_str = ['1', '2', '3', '4', '5']
number_int = map(int, numbers_str)
print(list(number_int))


# with names
def change_to_upper(name):
    return name.upper()

names = ['Diego', 'Amanda', 'Vivian', 'Fernando']

names_upper_cased1 = map(change_to_upper, names)
print(list(names_upper_cased1))

names_upper_cased = map(lambda name: name.upper(), names)
print(list(names_upper_cased)) # map = muda uma lista com uma função e retorna uma lista nova.