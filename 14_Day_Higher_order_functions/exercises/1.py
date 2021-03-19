#map
numbers = [1, 2, 3]

def multipliqueby2(n):
    return n * 2

new_numbers = map(multipliqueby2, numbers) # receive function and list and execute a order by each value in the list
print(list(new_numbers))

#filter
languages = ['Python', 'JavaScript', 'PHP', 'Java', 'C++', 'C#']

def best_language(lng):
    if lng == 'Python':
        return True
    else:
        return False

best_programming_language = filter(best_language, languages) # verify if is true and return True itens inside a list
print(list(best_programming_language))

#reduce
from functools import reduce

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def total_of_list(func, list):
    return int(func) + int(list)

total = reduce(total_of_list, numbers) # return a value from function and list
print(total)
