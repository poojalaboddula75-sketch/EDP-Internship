import pandas as pd
import matplotlib.pyplot as plt

# Load prediction results
df = pd.read_csv("predictions.csv")

print("WEEK 7 - PREDICTION ERROR ANALYSIS")
print("-----------------------------------")

print("\nPREDICTION RESULTS")
print(df)

# Calculate prediction error
df["Error"] = df["ActualMarks"] - df["PredictedMarks"]

# Calculate absolute error
df["AbsoluteError"] = df["Error"].abs()

print("\nERROR ANALYSIS")
print(df)

# Calculate average absolute error
mae = df["AbsoluteError"].mean()

print("\nMean Absolute Error:", mae)

# Find maximum error
max_error = df["AbsoluteError"].max()

print("Maximum Absolute Error:", max_error)

# Plot actual vs predicted
plt.figure(figsize=(8, 6))

plt.scatter(
    df["ActualMarks"],
    df["PredictedMarks"]
)

minimum = min(
    df["ActualMarks"].min(),
    df["PredictedMarks"].min()
)

maximum = max(
    df["ActualMarks"].max(),
    df["PredictedMarks"].max()
)

plt.plot(
    [minimum, maximum],
    [minimum, maximum],
    linestyle="--"
)

plt.xlabel("Actual Marks")
plt.ylabel("Predicted Marks")
plt.title("Week 7 - Predicted vs Actual Marks")
plt.grid(True)
plt.tight_layout()

plt.savefig("week7_predicted_vs_actual.png")

print("\nVisualization saved as week7_predicted_vs_actual.png")

plt.show()