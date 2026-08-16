import pandas as pd

print("===== MOTOR SENSOR DATA ANALYSIS =====")

df = pd.read_csv("week2/day6/motor_data.csv")

print("\nOriginal Data:")
print(df)

# Program 1 - High Temperature
print("\n===== HIGH TEMPERATURE RECORDS =====")

high_temp_records = df[df["Temperature"] > 70]
print(high_temp_records)

# Program 2 - High Current
print("\n===== HIGH CURRENT RECORDS =====")

high_current_records = df[df["Current"] > 9]
print(high_current_records)

# Program 3 - Sorting
print("\n===== SORT BY TEMPERATURE =====")
print(df.sort_values("Temperature"))

print("\n===== SORT BY CURRENT =====")
print(df.sort_values("Current"))

print("\n===== SORT BY RPM =====")
print(df.sort_values("RPM"))

print("\n===== TEMPERATURE - DESCENDING =====")
print(df.sort_values("Temperature", ascending=False))

# Program 4 - Missing Data
print("\n===== MISSING DATA =====")

missing_data = df.isnull().sum()
print(missing_data)

# Small Challenge
print("\n===== MOTOR RECORDS ABOVE NORMAL TEMPERATURE =====")

threshold_temp = float(
    input("Enter the temperature threshold: ")
)

above_normal_temp_records = df[
    df["Temperature"] > threshold_temp
]

print(above_normal_temp_records)