import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

# Sample dataset (house size vs. price)
data = {
    "Square_Feet": [600, 800, 1000, 1200, 1500, 1800, 2000, 2500, 3000],
    "Price": [150, 180, 220, 260, 300, 350, 400, 500, 600]
}

df = pd.DataFrame(data)

# Splitting data into features (X) and target (Y)
X = df[["Square_Feet"]]
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

# Plot data points
plt.scatter(X, y, color="blue", label="Actual Data")
plt.plot(X, model.predict(X), color="red", label="Regression Line")
plt.xlabel("Square Footage")
plt.ylabel("Price")
plt.title("Linear Regression: House Price Prediction")
plt.legend()
plt.show()
