import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Generate sample data
x_values = np.linspace(-1.2, 0.0002, 100).reshape(-1, 1)  # x values from -1.2 to 0.0002
y_values = 2.5 * x_values + np.random.normal(0, 0.2, x_values.shape)  # y = 2.5x + noise

# Create a linear regression model and fit it to the data
model = LinearRegression()
model.fit(x_values, y_values)
y_pred = model.predict(x_values)

# Plotting
plt.scatter(x_values, y_values, color='blue', label='Data Points')
plt.plot(x_values, y_pred, color='red', label='Regression Line')

# Adding labels
plt.xlabel('X values')
plt.ylabel('Y values')
plt.title('Linear Regression Plot')
plt.legend()

# Save plot to file
plt.savefig('pyplot_graph.png')

# Show plot
plt.show()