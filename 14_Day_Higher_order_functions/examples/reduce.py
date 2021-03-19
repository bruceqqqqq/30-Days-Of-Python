from functools import reduce

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers_str = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

def add_two_nums(x, y):
    return int(x) + int(y)

total = reduce(add_two_nums, numbers)
print(total)
total = reduce(add_two_nums, numbers_str)
print(total)
