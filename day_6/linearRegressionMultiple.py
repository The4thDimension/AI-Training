# Experiment with multiple features (e.g., Square_Feet & Bedrooms → Price).
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
import numpy as np

# Sample dataset (house size vs. price)
data = {
    "Square_Feet": [600, 800, 1000, 1200, 1500, 1800, 2000, 2500, 3000],
    "Bedroom_Count": [1, 1, 2, 2, 3, 3, 4, 4, 5],
    "Price": [150, 180, 220, 260, 300, 350, 400, 500, 600]
}

df = pd.DataFrame(data)

# Splitting data into features (X) and target (Y)
X = df[["Square_Feet", "Bedroom_Count"]]
y = df["Price"]

# Split into training (80%) and testing (20%) sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate model performance
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse}")

# Print model parameters
print(f"Intercept: {model.intercept_}")
print(f"Slope: {model.coef_[0]}")

# Create a 3D plot
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection="3d")

# Scatter plot of actual data
ax.scatter(df["Square_Feet"], df["Bedroom_Count"], y, color="blue", label="Actual Data")

# Generate a grid of values for prediction
square_feet_range = np.linspace(df["Square_Feet"].min(), df["Square_Feet"].max(), 30)
bedroom_count_range = np.linspace(df["Bedroom_Count"].min(), df["Bedroom_Count"].max(), 30)
square_feet_grid, bedroom_count_grid = np.meshgrid(square_feet_range, bedroom_count_range)
X_pred_grid = np.c_[square_feet_grid.ravel(), bedroom_count_grid.ravel()]

# Predict prices for the grid
y_pred_grid = model.predict(X_pred_grid).reshape(square_feet_grid.shape)

# Plot regression surface
ax.plot_surface(square_feet_grid, bedroom_count_grid, y_pred_grid, color="red", alpha=0.5)

# Labels and title
ax.set_xlabel("Square Footage")
ax.set_ylabel("Bedroom Count")
ax.set_zlabel("Price")
ax.set_title("Multiple Linear Regression: House Price Prediction")
ax.legend()

plt.show()
