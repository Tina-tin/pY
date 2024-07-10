import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Generate some random data
np.random.seed(0)
X = np.random.rand(100, 1) * 10  # Random X values
y = 2 * X + 1 + np.random.randn(100, 1) * 2  # Linear relation with noise

# Create a linear regression model
model = LinearRegression()
model.fit(X, y)

# Generate new data points for prediction
X_new = np.linspace(0, 10, 100).reshape(-1, 1)

# Predict using the model
y_pred = model.predict(X_new)

# Plotting
plt.scatter(X, y, color='blue', label='Data Points')  # Scatter plot of the data
plt.plot(X_new, y_pred, color='red', label='Regression Line')  # Regression line

plt.xlabel('X')
plt.ylabel('y')
plt.title('Linear Regression Example')
plt.legend()

plt.show()