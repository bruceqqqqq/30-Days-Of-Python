import numpy as np

two_dimensional_arrays = np.array([(1,2,3),(4,5,6),(7,8,9)])

#gettings itens by row
first_row, second_row, third_row = two_dimensional_arrays[0], two_dimensional_arrays[1], two_dimensional_arrays[2]
print(first_row)
print(second_row)
print(third_row)

#gettings itens by columns

first_column, second_column, third_column = two_dimensional_arrays[:,0], two_dimensional_arrays[:,1], two_dimensional_arrays[:,2]
print(first_column)
print(second_column)
print(third_column)

#slicing numpy array

first_two_rows_and_columns = two_dimensional_arrays[0:2, 0:2]
print(first_two_rows_and_columns)
# reverse the row and column positions
print(two_dimensional_arrays[::-1,::-1])
# how change a value from array
two_dimensional_arrays[1, 1] =  55
two_dimensional_arrays[1, 2] =  44
print(two_dimensional_arrays)
numpy_zeros = np.zeros((3, 3), dtype=int, order='C') # TWODIMENSIONAL ARRAYS OF ZEROS
print(numpy_zeros)
numpy_ones = np.ones((3, 3), dtype=int, order='C') # TWODIMENSIONAL ARRAYS OF ONES
print(numpy_ones)
twoes = numpy_ones * 2 # TWODIMENSIONAL ARRAYS OF TWOS
print(twoes)
first_shape = np.array([(1,2,3),(4,5,6)])
print(first_shape)
reshaped = first_shape.reshape(3, 2)
print(reshaped)
flattened = reshaped.flatten()
print(flattened)
np1 = np.array([1,2,3])
np2 = np.array([4,5,6])
print(np1+np2)
print(np.hstack((np1, np2)))
print(np.vstack((np1, np2)))
