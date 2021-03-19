# List Comprehension Basic
language = 'Python'
lst = [i for i in language]
print(lst)

# Generating Numbers
numbers = [i for i in range(11)]
print(numbers)

# Square with LC
squares = [i * i for i in range(11)]
print(squares)

# List of Tuples with LC
numbers = [(i, i * i) for i in range(11)]
print(numbers)

# Lists of Even with LC
even_numbers = [i for i in range(11) if i % 2 == 0]
print(even_numbers)

# Lists of Odd with LC
odd_numbers = [i for i in range(11) if i % 2 != 0]
print(odd_numbers)

numbers = [-8, -7, -6, -5, 0, 2, 3, 7, 8, 9, 10]
positive_even_numbers = [i for i in numbers if i % 2 == 0 and i >= 0]
print(positive_even_numbers)

three_dimen_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9] ]
flattened_list = [n for r in three_dimen_list for n in r]
print(flattened_list)