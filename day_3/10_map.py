# Problem Statement
# 
# Write a function that takes a 2D NumPy array and returns an array where each element is the square of the original if it’s even, or the cube if it’s odd.

import numpy as np

def returnVal(x):
    if x % 2 == 0:
        return x * x
    else:
        return x * x * x
    
vectorReturnVal = np.vectorize(returnVal)

arr = np.array([[1, 2], [3, 4]])
newArr = vectorReturnVal(arr)
print(newArr)