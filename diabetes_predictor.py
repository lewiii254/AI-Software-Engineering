# diabetes_predictor.py

# Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix

# Load Dataset
df = pd.read_csv('diabetes.csv')  # Ensure this file is in your working directory

# Display first few rows
print("First 5 rows of dataset:")
print(df.head())

# Data Preprocessing
cols_with_zeros = ['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']
df[cols_with_zeros] = df[cols_with_zeros].replace(0, np.nan)

# Fill missing values with median
df.fillna(df.median(), inplace=True)

# Features and Target
X = df.drop('Outcome', axis=1)
y = df['Outcome']

# Standardize Features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)


# Split Data
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Train Model
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Evaluation Metrics
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# Confusion Matrix
cm = confusion_matrix(y_test, y_pred)
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
plt.title('Confusion Matrix')
plt.xlabel('Predicted')
plt.ylabel('True')
plt.show()

# Feature Importances
feature_importances = pd.Series(model.feature_importances_, index=df.columns[:-1]).sort_values(ascending=False)
print("\nFeature Importances:")
print(feature_importances)

# Plot Feature Importances
feature_importances.plot(kind='bar')
plt.title('Feature Importance in Diabetes Prediction')
plt.show()

# Save the model (Optional)
# import joblib
# joblib.dump(model, 'diabetes_model.pkl')
