add_two_nums = lambda a, b : a + b
print(add_two_nums(2, 3))
square = lambda x : x ** 2
print(square(3))
cube = lambda x : x ** 3
print(cube(3))
multiple_variable = lambda a, b, c: a ** 2 - 3 * b + 4 * c
print(multiple_variable(5, 5, 3))

def power(x):
    return lambda n : x ** n
cube = power(3)(3)
print(cube)