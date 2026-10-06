import pandas as pd

# Load dataset
df = pd.read_csv("student_data.csv")

print("STUDENT DATASET")
print(df)

# Dataset information
print("\nDATASET SHAPE")
print(df.shape)

print("\nCOLUMN NAMES")
print(df.columns)

# Features and target
features = [
    "StudyHours",
    "Attendance",
    "AssignmentScore",
    "PreviousMarks"
]

target = "Marks"

print("\nFEATURES")
print(features)

print("\nTARGET")
print(target)

# Feature data
X = df[features]

# Target data
y = df[target]

print("\nFEATURE DATA")
print(X)

print("\nTARGET DATA")
print(y)