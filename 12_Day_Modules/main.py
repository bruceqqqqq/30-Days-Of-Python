from mymodule import generate_full_name, sum_two_nums, person as p, pi
from statistics import *
import math
import string
import random
from math import pi

# import by a custom
print(generate_full_name('Diego', 'Fregolente'))
print(sum_two_nums(1, 9))
print(p)
print(p['age'])
area = pi * 30 ** 2
print(area)

# import by statistics
ages = [20, 21, 23, 22, 22, 24]
print(mean(ages))       # ~22.9
print(median(ages))     # 23
print(mode(ages))       # 20
print(stdev(ages))      # ~2.3

# import by math
print(math.pi)
print(math.sqrt(2)) # raiz quadrada
print(math.pow(2, 3)) # 2 ** 3
print(math.floor(9.81)) # arredondando pro menor
print(math.ceil(9.81)) # arredondando pro maior
print(math.log10(100)) # logarithim with 10 as base

# import by string
print(string.ascii_letters)
print(string.digits)
print(string.punctuation)

# import by random

print(random.random())
print(random.randint(1, 10))

# import PI from math

print(pi)
