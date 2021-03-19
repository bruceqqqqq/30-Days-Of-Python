import numpy as np

# print('numpy:', np.__version__)
# print(dir(np))

# Listas de Python Normal
python_list = [1, 2, 3, 4, 5]
two_dimensional_list = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]

# Criando um numpy (numeral python) array de uma python list
numpy_array_from_list_with_int = np.array(python_list)

# Criando uma numpy float array
numpy_array_from_list_with_float = np.array(python_list, dtype=float)

# Criando uma numpy boolean array
numpy_array_from_list_with_bool = np.array([0, 1, -1, 0,0 ], dtype=bool)

# Criando multidimensional numpypy array
numpy_two_dimensional_list = np.array(two_dimensional_list)

# Revertendo np array for list
numpy_to_list = numpy_array_from_list_with_int.tolist()


# Criando uma numpy array from tuple
python_tuple = (1, 2, 3, 4, 5)
numpy_array_from_tuple = np.array(python_tuple)

# Shape of numpy array
nums = np.array([1, 2, 3, 4, 5])
# print(nums)
# print(nums.shape) # (5,) 5 columns because has no rows
# print(numpy_two_dimensional_list)
# print(numpy_two_dimensional_list.shape) # (3, 3) 3 rows, 3 columns
three_by_four_array = np.array([[0, 1, 2, 3],
                                [4, 5, 6, 7],
                              [8, 9, 10, 11]]) # 3 rows, 4 columns,
# print(three_by_four_array.shape)

# Data type of numpy array
# Type of data types: str, int, float, complex, bool, list, None
int_lists = [-3, -2, -1, 0, 1, 2, 3]
int_array = np.array(int_lists)
float_array = np.array(int_lists, dtype=float)
# print(int_array.dtype)
# print(float_array.dtype)

# Size of a numpy array
num_array_from_list = np.array([1, 2, 3, 4, 5])
two_dimensional_list = np.array([[0,1,2],
                                 [3,4,5],
                                 [6,7,8]])
# print(num_array_from_list.size)
# print(two_dimensional_list.size)
