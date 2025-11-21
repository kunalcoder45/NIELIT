# Numpy Broadcasting means the ability of numpy to treat arrays of different shapes during arithmetic operations.
# The smaller array is "broadcast" across the larger array so that they have compatible shapes.

import numpy as np

# a = np.array([[1, 2, 3],
#                 [4, 5, 6],
#                 [7, 8, 9]])
# b = np.array([10, 20, 30])
# result = a + b
# print("Array a:")
# print(a) 
# print("Array b:")
# print(b)
# print("Result of a + b:")
# print(result)


# a = np.array([[1, 2, 3],
#                 [4, 5, 6],
#                 [7, 8, 9]])
# print(a)
# for x in np.nditer(a):
#     print(x, end=', ')