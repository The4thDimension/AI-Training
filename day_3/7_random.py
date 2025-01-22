# Problem Statement
# Generate a 4x4 matrix of random integers between 1 and 100.
# Find the maximum and minimum values along each column.


import random
import numpy as np

def getRandomNum():
    return int(random.random() * 100)

arr = np.array([[getRandomNum(), getRandomNum(), getRandomNum(), getRandomNum()], [getRandomNum(), getRandomNum(), getRandomNum(), getRandomNum()], [getRandomNum(), getRandomNum(), getRandomNum(), getRandomNum()], [getRandomNum(), getRandomNum(), getRandomNum(), getRandomNum()]])

print(arr)

max_col_vals = np.amax(arr, axis=0)
print(max_col_vals)