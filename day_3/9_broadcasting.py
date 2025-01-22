# Problem Statement: 
# 
# Create a 3x3 matrix and a 1D array with 3 elements. Add the 1D array to each row of the matrix using broadcasting.


import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
arr1 = np.array([10, 11, 12])
newArr = arr + arr1
print(newArr)