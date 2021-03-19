import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import random

normal_array = np.random.normal(79, 15, 80)

sns.set()
plt.hist(normal_array, color='grey', bins=50)

four_by_four_matrix = np.matrix(np.ones((4,4), dtype=float))

np.asarray(four_by_four_matrix)[2] = 2 # 3 row mude pra 2

whole_numbers = np.arange(2, 20, 2)

np.linspace(1.0, 5.0, num=10)

np.linspace(1.0, 5.0, num=5, endpoint=False)

natural_numbers = np.arange(1, 20, 1)

odd_numbers = np.arange(1, 20, 2)

even_numbers = np.arange(2, 20, 2)

np.logspace(2, 4.0, num=4)

x = np.array([1,2,3], dtype=np.complex128)
# print(x.itemsize)

np_list = np.array(([1,2,3], [4,5,6]))
print(np_list[0])
print(np_list[1])
print(np_list[:,0])
print(np_list[:,1])
print(np_list[:,2])