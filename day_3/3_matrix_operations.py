# Problem Statement:
# Create two 2x2 matrices and perform matrix multiplication.
# Transpose one of the matrices and print the result.


import numpy as np
mat_1 = np.array([[1, 2], [3, 4]])
mat_2 = np.array([[5, 6], [7, 8]])
mat_mul = mat_1.dot(mat_2)
mat_transpose = mat_1.transpose()
print(mat_mul)
print(mat_transpose)