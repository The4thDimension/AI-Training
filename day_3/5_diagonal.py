# Problem Statement
# Create a 5x5 matrix and slice out the first 2 rows and last 2 columns.
# Retrieve the diagonal elements of the matrix.


import numpy as np

var = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]])
var = var[2:, :-2]
diag_var = np.diag(var)
print(var)
print(diag_var)