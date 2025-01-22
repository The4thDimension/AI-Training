# Problem Statement
# Create a 1D array with 12 elements and reshape it into a 3x4 matrix.
# Flatten the matrix back into a 1D array.


import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newArr = arr.reshape(3, 4)
print(newArr)
flatArr = newArr.flatten()
print(flatArr)