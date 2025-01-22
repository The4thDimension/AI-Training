# Problem Statement
# Create an array of numbers from 1 to 10. Identify which elements are greater than 5.


import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(arr[arr > 5])