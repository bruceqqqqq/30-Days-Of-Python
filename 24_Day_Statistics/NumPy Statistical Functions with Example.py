import numpy as np
import statistics
import matplotlib.pyplot as plt
import seaborn as sns


np_normal_dis = np.random.normal(5, 0.5, 100)
print(np_normal_dis.min())
print(np_normal_dis.max())
print(np_normal_dis.mean())
# print(np_normal_dis.median()) # not working
print(np_normal_dis.std())

two_dimension_array = np.array([(1,2,3), [4,5,6]])
print(two_dimension_array)
print('Max row:', np.amax(two_dimension_array, axis=0))
print('Max column:', np.amax(two_dimension_array, axis=1))
print('Min column:', np.amin(two_dimension_array, axis=0))
print('Min column:', np.amin(two_dimension_array, axis=1))

a = [1, 2, 3]
print('Tile:', np.tile(a, 2)) # just repeat a list
print('Repeat:', np.repeat(a, 2)) # sort repeat

print(np.random.random()) # between 0 - 1
r = np.random.random(size=[2, 3]) # 2 row 3 column
print(r)

print(np.random.choice(['a', 'e', 'i', 'o', 'u'], size=10)) # escolhe 10 vezes algo da lista
print(np.random.choice([1, 2, 3, 4, 5], size=10)) # escolhe 10 vezes algo da lista

print(np.random.rand(2,2))
print(np.random.randn(2,2))
print(np.random.randint(0, 10, size=[5,3]))

from scipy import stats

np_normal_dis = np.random.normal(5, 0.5, 1000)
print(np.max(np_normal_dis))
print(np.min(np_normal_dis))
print(np.mean(np_normal_dis))
print(np.mean(np_normal_dis))
print(np.median(np_normal_dis))
print(stats.mode(np_normal_dis))
print(np.std(np_normal_dis))

plt.hist(np_normal_dis, color='grey', bins=21)
plt.show()

