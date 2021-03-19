import random
import numpy as np

random_float = np.random.random()
print(random_float) # random number
random_float = np.random.random(5)
print(random_float) # numpy array with 5 numbers floats
random_int = np.random.randint(0, 11)
print(random_int) # random number between 0 and 10
random_int = np.random.randint(2, 10, size=4)
print(random_int) # one row array with 4 numbers between 2 and 9
random_int = np.random.randint(2, 10, size=(3, 3))
print(random_int) # random int array with 3 rows ans 3 columns between 2 and 9
normal_array = np.random.normal(3, 2.5, (2,4))
print(normal_array)
normal_array = np.random.normal(10, 10, 5)
print(normal_array)