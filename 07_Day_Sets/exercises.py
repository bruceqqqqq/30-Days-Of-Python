# Sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print(f'Lenght of it_companies {len(it_companies)}') # 1

it_companies.add('Twitter')
print(it_companies) # 2

it_companies.update(['Infosys', 'HP', 'Dell', 'Accenture'])
print(it_companies) # 3

it_companies.remove('Accenture') # 4 remove, if value not in set raise a error

it_companies.discard('Accenture') # 5 discard, try to remove if value not in set, just do nothing and dont raise errors.
print(it_companies)

print(A.union(B)) # 6 Join B in A

print(A.intersection(B)) # 7 Return items who are in both

print(A.issubset(B)) # 8 if all items of 'set'.issubset('otherset') return True else False

print(A.isdisjoint(B)) # 9 if have no common values return True else False

A.update(B), B.update(A)

print(A.symmetric_difference(B)) # return set() if has no difference

del A
del B

print(len(age))

ageSet = set(age)

print(len(ageSet)) # less

# String = s any type of data enclosed in quotes exemple '1' 'AB' '!@#!#!'
# List = Can be any type of data, ordered and can be manipulated, list of values
# Tuple = same as list, but can not be manipulated remove or add itens, if you need to change tuple, convert to list.
# Set = like a list, but have only unique values and have anothers functions

phrase = {'I', 'am', 'teacher', 'and', 'I', 'love', 'to', 'inspire', 'and', 'teach', 'people'}
print(phrase)
print('Unique words: ', len(phrase))
