import pandas as pd

# Load the dataset
df = pd.read_csv("students.csv")

print("ORIGINAL DATA")
print(df)

# Check missing values
print("\nMISSING VALUES")
print(df.isnull().sum())

# Check duplicate rows
print("\nDUPLICATE ROWS")
print(df.duplicated().sum())

# Remove duplicate rows
df = df.drop_duplicates()

print("\nDATA AFTER CLEANING")
print(df)

# Save cleaned dataset
df.to_csv("students_cleaned.csv", index=False)

print("\nCleaned dataset saved successfully.")