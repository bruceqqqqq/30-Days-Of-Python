# only even numbers

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False

even_numbers = filter(is_even, numbers)
print(list(even_numbers))

def is_odd(num):
    if num % 2 != 0:
        return True
    else:
        return False

odd_numbers = filter(is_odd, numbers)
print(list(odd_numbers))


names = ['Diego', 'Vivian', 'Amanda', 'Fernando']

def is_name_long(name):
    if len(name) > 5:
        return True
    else:
        return False

long_name = filter(is_name_long, names)
print(list(long_name))
