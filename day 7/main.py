import numpy as np

# 1) np.empty function
# arr = np.empty((3, 2), dtype=int)
# print("Empty array of shape (3,2) with integer type:\n", arr)

# output me jo numbers hain wo random hote hain kyunki memory allocation ke time pe unhe initialize nahi kiya gaya hota hai. empty function sirf memory allocate karta hai bina kisi initial value ke.


# NOTE ---------------------------------------------------------------------------------------------------------------------------
# C style means row-major order hota hai, jisme pehle rows ko store kiya jata hai. For example, agar humare paas ek 2D array hai:
# [[1, 2, 3], 
#  [4, 5, 6]]
# toh C style me ye memory me is tarah store hoga: 1, 2, 3, 4, 5, 6.

# ( F ) Fortran style means column-major order hota hai, jisme pehle columns ko store kiya jata hai. Usi 2D array ke case me:
# [[1, 2, 3],
#  [4, 5, 6]]
# Fortran style me ye memory me is tarah store hoga: 1, 4, 2, 5, 3, 6.

# -----------------------------------------------------------------------------------------------------------------------------
# 2) np.zeros function
# arr = np.zeros((3, 2), dtype=int)
# print(arr)

# 3) np.ones function
# arr = np.ones((3, 2), dtype=int)
# print(arr)


# 4) asarray function, using tuple conversion to array

# tup = (1, 2, 3, 4, 5)

# a = np.asarray(tup)
# print("Array from list:\n", a)
# print("Type of a:", type(a))

# 5) np.arange function

# arr = np.arange(10, 20, 2)
# print("Array with values from 10 to 20 with step 2:", arr)

# arange(10, 20, 2) ka matlab hai 10 se start karna, 20 se pehle tak jana, aur har step me 2 add karna.

