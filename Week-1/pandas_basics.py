import pandas as pd

# Load dataset
df = pd.read_csv("students.csv")

print("STUDENT DATASET")
print(df)

print("\nFIRST FIVE ROWS")
print(df.head())

print("\nDATASET SHAPE")
print(df.shape)

print("\nCOLUMN NAMES")
print(df.columns)

print("\nDATASET INFORMATION")
df.info()

print("\nSTATISTICAL SUMMARY")
print(df.describe())

# Features and Target
features = ["StudyHours", "Attendance", "AssignmentScore"]
target = "Marks"

print("\nFEATURES")
print(features)

print("\nTARGET")
print(target)