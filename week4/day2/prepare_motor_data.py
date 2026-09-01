#Day 2 – Preparing the Motor Dataset
"""Create: 
prepare_motor_data.py 

The program should: 
    1. Load the dataset.
    2. Clean the dataset.
    3. Select features.  
    4. Select target.  
    5. Split training/testing data. 
"""

import pandas as pd

print("===== MOTOR DATA PREPARATION =====")


# STEP 1 — Load the dataset
df = pd.read_csv("week4/day1/ai4i2020.csv")

print("\nOriginal Dataset Shape:")
print(df.shape)


# STEP 2 — Check missing values
print("\n===== MISSING VALUES =====")
missing_values = df.isnull().sum()
print(missing_values)


# STEP 3 — Check duplicate records
print("\n===== DUPLICATE RECORDS =====")
duplicate_count = df.duplicated().sum()
print(f"Number of duplicate records: {duplicate_count}")


# STEP 4 — Check data types
print("\n===== DATA TYPES =====")
print(df.dtypes)


# STEP 5 — Identify categorical and numerical columns

categorical_columns = df.select_dtypes(
    include=["object", "str"]
).columns.tolist()

numerical_columns = df.select_dtypes(
    include=["number"]
).columns.tolist()

print("\nCategorical Columns:")
print(categorical_columns)

print("\nNumerical Columns:")
print(numerical_columns)


# STEP 6 — Select features and target

X = df[
    [
        "Type",
        "Air temperature [K]",
        "Process temperature [K]",
        "Rotational speed [rpm]",
        "Torque [Nm]",
        "Tool wear [min]"
    ]
]

y = df["Machine failure"]


print("\n===== FEATURES (X) =====")
print(X.head())

print("\n===== TARGET (y) =====")
print(y.head())


# STEP 7 — Train/Test Split

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


print("\n===== TRAIN/TEST SPLIT =====")
print(f"Training records: {len(X_train)}")
print(f"Testing records: {len(X_test)}")