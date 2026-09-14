# Program 1 – Find Failure Cases 
"""
Explore the dataset and identify: 
• How many machines/motors failed?  
• How many did not fail?  
• What percentage failed?  
• Which sensor readings are present before failure? 
"""

import pandas as pd

print("===== MOTOR FAILURE CASES ANALYSIS =====")

# Load the AI4I Dataset
df = pd.read_csv("week4/day1/ai4i2020.csv")
print("\nOriginal Data")
print(df)

print("\n===== DATASET INFORMATION =====")
print(f"Total records: {len(df)}")
print(f"Total columns: {len(df.columns)}")

# Count Failures and non-failures cases
failure_count = (df["Machine failure"] == 1).sum()
normal_count = (df["Machine failure"] == 0).sum()

failure_percentage = (failure_count/len(df))*100

print("\n===== FAILURE SUMMARY =====")
print(f"Motors with failure: {failure_count}")
print(f"Motors without failure: {normal_count}")
print(f"The failure percentage: {failure_percentage:.2f}%")

# Show available motor operating parameters
print("\n===== AVAILABLE SENSOR/OPERATING DATA =====")

sensor_columns = [
    "Air temperature [K]",
    "Process temperature [K]",
    "Rotational speed [rpm]",
    "Torque [Nm]",
    "Tool wear [min]"
]

for column in sensor_columns:
    print("-", column)

# Display some failure records
print("\n===== EXAMPLE FAILURE RECORDS =====")

failure_cases = df[df["Machine failure"] == 1]

print(failure_cases[
    [
        "UDI",
        "Type",
        "Air temperature [K]",
        "Process temperature [K]",
        "Rotational speed [rpm]",
        "Torque [Nm]",
        "Tool wear [min]",
        "Machine failure"
    ]
].head(20)
)
