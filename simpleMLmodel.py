# simple ML model using the scikit-learn library to predict house prices based on features like size and number of bedrooms.
# Import necessary libraries
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import numpy as np

# Sample data: [size (sq ft), number of bedrooms]
X = np.array([[1400, 3], [1600, 4], [1700, 3], [1875, 4], [1100, 2]])
y = np.array([245000, 312000, 279000, 308000, 199000])  # Prices in USD

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Make a prediction
predicted_price = model.predict([[1500, 3]])
print(f"Predicted Price: ${predicted_price[0]:.2f}")