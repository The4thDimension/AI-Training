import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

X = np.array([1, 2, 3, 4, 5])
Y = np.array([2, 4, 5, 4, 5])

m, b = np.polyfit(X, Y, 1)

plt.scatter(X, Y, color="blue", label="Data Points")
plt.plot(X, m*X + b, color="red", label="Regression Line")

plt.xlabel("Square Footage")
plt.ylabel("House Price")
plt.title("Example")
plt.legend()
plt.show()