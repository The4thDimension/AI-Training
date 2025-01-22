# Problem Statement
# Create an array with at least 10 random numbers. Calculate the mean, median, variance, and standard deviation.


import numpy as np
arr = np.array([2, 5, 1, 6, 6, 4, 8, 8, 4, 9, 5, 1, 0])
mean_val = np.mean(arr)
median_val = np.median(arr)
variance_val = np.var(arr)
std_dev = np.std(arr)
print(mean_val)
print(median_val)
print(variance_val)
print(std_dev)