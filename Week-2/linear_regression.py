import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Load dataset
df = pd.read_csv("student_performance.csv")

print("DATASET")
print(df)

# Feature and target
X = df[["StudyHours"]]
y = df["Marks"]

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create and train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluation
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("\nACTUAL VALUES")
print(y_test.values)

print("\nPREDICTED VALUES")
print(y_pred)

print("\nMODEL EVALUATION")
print("MAE:", mae)
print("MSE:", mse)
print("R2 Score:", r2)

print("\nSLOPE:", model.coef_[0])
print("INTERCEPT:", model.intercept_)