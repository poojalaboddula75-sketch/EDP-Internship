# EDP Internship - Week 1

## Topic
Pandas Basics and Data Cleaning

## Objective
The objective of this week's work is to learn the basics of Pandas, load a sample dataset, inspect the data, identify features and target, and perform basic data cleaning.

## Tools Used
- Python 3.13.7
- Pandas 3.0.5
- VS Code

## Work Completed

### 1. Pandas Basics
- Imported Pandas library.
- Loaded a CSV dataset using `pd.read_csv()`.
- Displayed the complete dataset.
- Viewed the first five rows using `head()`.
- Checked dataset shape using `shape`.
- Identified column names.
- Checked data types and dataset information using `info()`.
- Generated statistical summary using `describe()`.

### 2. Features and Target
The selected features are:
- StudyHours
- Attendance
- AssignmentScore

The target variable is:
- Marks

### 3. Data Cleaning
- Checked for missing values using `isnull().sum()`.
- Checked for duplicate rows using `duplicated().sum()`.
- Removed duplicate rows using `drop_duplicates()`.
- Saved the cleaned dataset as `students_cleaned.csv`.

## Dataset
The sample dataset contains student study hours, attendance, assignment scores, and marks.

## Files
- `students.csv` - Original sample dataset
- `students_cleaned.csv` - Cleaned dataset
- `pandas_basics.py` - Pandas dataset analysis
- `data_cleaning.py` - Data cleaning operations

## Result
Successfully loaded, inspected, analyzed, and cleaned the sample student dataset using Python and Pandas.