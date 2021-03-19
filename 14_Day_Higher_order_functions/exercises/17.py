from functools import reduce

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']

sentence = reduce(lambda x, y: x + ', ' + y, countries) + ' are north European countries.'

print(sentence)