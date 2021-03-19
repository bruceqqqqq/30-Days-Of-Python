import numpy as np

numpy_int_arr = np.array([1, 2, 3, 4])
numpy_float_arr = np.array([1.0, 2.0, 3.0, 4.0])
numpy_bool_arr = np.array([-3, -2, 0, 1, 2, 3], dtype='bool') # 0 false / int negative or positive true

# print(numpy_int_arr.dtype)
# print(numpy_float_arr.dtype)
# print(numpy_bool_arr.dtype)

# int to float
int_to_float = np.array(numpy_int_arr, dtype='float')
# float to int
float_to_int = np.array(int_to_float, dtype='int')
# int to bool
int_to_bool = np.array(float_to_int, dtype='bool')
# int to str
int_to_str = np.array(numpy_int_arr.astype('int').astype('str'))
print(int_to_str)