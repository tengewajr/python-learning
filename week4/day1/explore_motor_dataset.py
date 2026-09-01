import pandas as pd

print("===== AI4I 2020 PREDICTIVE MAINTENANCE DATASET =====")

# Load dataset
df = pd.read_csv("week4/day1/ai4i2020.csv")

# First 5 rows
print("\n===== FIRST 5 ROWS =====")
print(df.head())

# Last 5 rows
print("\n===== LAST 5 ROWS =====")
print(df.tail())

# Number of rows
print("\n===== NUMBER OF ROWS =====")
print(len(df))

# Number of columns
print("\n===== NUMBER OF COLUMNS =====")
print(len(df.columns))

# Column names
print("\n===== COLUMN NAMES =====")
print(df.columns.tolist())

# Data types
print("\n===== DATA TYPES =====")
print(df.dtypes)

# Missing values
print("\n===== MISSING VALUES =====")
print(df.isnull().sum())