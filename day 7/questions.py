# 1.	Create two array of size (3, 3) and print their sum and multiplication.
import numpy as np

# arr1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# arr2 = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])
# sum_array = arr1 + arr2
# multiply_array = arr1 * arr2
# print("Sum of the two arrays:\n", sum_array)
# print("Multiply of the two arrays:\n", multiply_array)

# 2.	Create an array of size 10 and calculate square root and standard deviation.

# arr3 = np.arange(10)
# sqrt_array = np.sqrt(arr3)
# std_dev = np.std(arr3)
# print("Square root of the array:\n", sqrt_array)
# print("Standard deviation of the array:\n", std_dev)

# 3.	Print size and dimension of above arrays.
# arr1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# print("Size of arr1:", arr1.size)
# print("Dimension of arr1:", arr1.ndim)

# 4.	Create a numpy array with following columns: hindi, English, science, math and commerce with data type int32. 
# a.	Insert at least 10 rows in the above array.
# b.	Display size and shape of the array.
# c.	Print sum of each column.
# d.	Print maximum element from each column.
# e.	Print sum of 1,4,5 row.

# data = np.array([
#     [85, 90, 78, 88, 92],
#     [76, 85, 80, 79, 84],
#     [90, 92, 88, 91, 95],
#     [65, 70, 72, 68, 74],
#     [88, 86, 84, 89, 90],
#     [92, 94, 96, 93, 91],
#     [75, 80, 78, 77, 79],
#     [83, 85, 87, 82, 81],
#     [91, 89, 90, 92, 93],
#     [78, 76, 74, 80, 77]
# ], dtype=np.int32)
# print("Size of the array:", data.size)
# print("Shape of the array:", data.shape)
# print("Sum of each column:", np.sum(data, axis=0))
# print("Maximum element from each column:", np.max(data, axis=0))
# print("Sum of 1, 4, 5 rows:", np.sum(data[[0, 3, 4]], axis=0))

# 5.	Create an array of size (3, 4) and reshape to (4, 3).

# arr4 = np.arange(12).reshape(3, 4)
# reshaped_arr = arr4.reshape(4, 3)
# print("Original array of shape (3,4):\n", arr4)
# print("Reshaped array of shape (4,3):\n", reshaped_arr)

