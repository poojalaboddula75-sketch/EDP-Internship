import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


# Load dataset
df = pd.read_csv("student_data.csv")

print("STUDENT GRADE PREDICTOR - WEEK 5")
print("\nDATASET")
print(df)


# Features and target
features = [
    "StudyHours",
    "Attendance",
    "AssignmentScore",
    "PreviousMarks"
]

target = "Marks"

X = df[features]
y = df[target]


# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42
)


# Standardize features
scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)


# -----------------------------
# Linear Regression - Baseline
# -----------------------------

linear_model = LinearRegression()
linear_model.fit(X_train_scaled, y_train)

linear_predictions = linear_model.predict(X_test_scaled)


# -----------------------------
# Ridge Regression
# -----------------------------

ridge_model = Ridge(alpha=1.0)
ridge_model.fit(X_train_scaled, y_train)

ridge_predictions = ridge_model.predict(X_test_scaled)


# -----------------------------
# Lasso Regression
# -----------------------------

lasso_model = Lasso(alpha=0.1)
lasso_model.fit(X_train_scaled, y_train)

lasso_predictions = lasso_model.predict(X_test_scaled)


# Evaluation function
def evaluate_model(model_name, actual, predicted):

    mae = mean_absolute_error(actual, predicted)
    mse = mean_squared_error(actual, predicted)
    r2 = r2_score(actual, predicted)

    print(f"\n{model_name}")
    print("-" * 30)
    print("MAE:", mae)
    print("MSE:", mse)
    print("R2 Score:", r2)

    return mae, mse, r2


# Evaluate models
linear_results = evaluate_model(
    "Linear Regression",
    y_test,
    linear_predictions
)

ridge_results = evaluate_model(
    "Ridge Regression",
    y_test,
    ridge_predictions
)

lasso_results = evaluate_model(
    "Lasso Regression",
    y_test,
    lasso_predictions
)


# Compare R2 scores
print("\nMODEL COMPARISON")
print("------------------------------")
print("Linear Regression R2:", linear_results[2])
print("Ridge Regression R2:", ridge_results[2])
print("Lasso Regression R2:", lasso_results[2])


# Select best model based on R2
models = {
    "Linear Regression": linear_results[2],
    "Ridge Regression": ridge_results[2],
    "Lasso Regression": lasso_results[2]
}

best_model = max(models, key=models.get)

print("\nBEST MODEL")
print(best_model)


# Save Ridge predictions for Week 6 visualization
prediction_output = pd.DataFrame({
    "ActualMarks": y_test.values,
    "PredictedMarks": ridge_predictions
})

prediction_output.to_csv(
    "predictions.csv",
    index=False
)

print("\nPredictions saved to predictions.csv")