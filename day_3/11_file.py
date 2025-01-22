# Problem Statement
# 
# Load a CSV file into a NumPy array (you can use np.genfromtxt()).
# Calculate the average of a specific column.
# Identify and count any missing values.

import numpy as np
import csv

arr = np.genfromtxt(("\t".join(i) for i in csv.reader(open('demoFile.csv'))), delimiter="\t")
print(arr)

mealCol = np.mean(arr[:, 0:1], axis=0)
print(mealCol)

numNaN = np.count_nonzero(np.isnan(arr))
print(numNaN)