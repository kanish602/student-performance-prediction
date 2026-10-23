
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score
import joblib

# Load student dataset
data = pd.read_csv("student-mat.csv", sep=";")

# Select input features and target
X = data[["studytime", "absences", "G1", "G2"]]
y = data["G3"]

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train the model
model = RandomForestRegressor(
    n_estimators=200, random_state=42
)
model.fit(X_train, y_train)

# Evaluate the model
predictions = model.predict(X_test)
print("Mean Absolute Error:", mean_absolute_error(y_test, predictions))
print("R2 Score:", r2_score(y_test, predictions))

# Save the trained model
joblib.dump(model, "model.pkl")
print("Model saved successfully!")

