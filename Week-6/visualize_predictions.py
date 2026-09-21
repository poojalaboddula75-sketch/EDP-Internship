import pandas as pd
import matplotlib.pyplot as plt


# Load prediction results
df = pd.read_csv("predictions.csv")

print("PREDICTION RESULTS")
print(df)


# Create Predicted vs Actual plot
plt.figure(figsize=(8, 6))

plt.scatter(
    df["ActualMarks"],
    df["PredictedMarks"]
)

# Ideal prediction line
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

plt.title("Predicted vs Actual Student Marks")

plt.grid(True)

plt.tight_layout()

# Save graph
plt.savefig("predicted_vs_actual.png")

plt.show()

print("\nVisualization saved as predicted_vs_actual.png")