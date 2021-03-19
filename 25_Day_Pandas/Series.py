import pandas as pd
import numpy as np

# Pandas Series Default
nums = [1, 2, 3, 4, 5]
s = pd.Series(nums) # index / value / int64 / default index
# Pandas Series Custom
fruits = ['Orange', 'Banana', 'Manga']
fruits = pd.Series(fruits, index=[1,2,3]) # index / value / object / custom index
# Pandas Series Dict
dct = dict(name='Diego', country='Brasil', city='São Paulo')
s = pd.Series(dct)
# Constant Pandas Series
s = pd.Series(10, index=[1, 2, 3])
# Pandas Series using Linspace
s = pd.Series(np.linspace(5, 20, 10), index=[i+1 for i in range(10)])




