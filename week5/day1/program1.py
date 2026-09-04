# Program 1 – Load & Sort Sensor Data 
"""Use Pandas to: 
• Load the dataset.  
• Convert the time column into a datetime format.  
• Sort records chronologically.  
• Display the earliest and latest readings
"""

import pandas as pd

print("===== TIME-SERIES MOTOR DATA ANALYSIS =====")

# Load the motor sensor dataset
df = pd.read_csv("week5/day1/motor_sensor_data.csv")

print("\nOriginal Data:")
print(df)

# Convert the time column into a datetime format
# A simulated date is added because the original dataset contains only time values.
df["Time"] = pd.to_datetime(
    "2026-09-04 " + df["Time"], format="%Y-%m-%d %H:%M"
)

# Sort records chronologically
df = df.sort_values("Time")

print("\n===== SORTED DATA =====")
print(df.head())

# The simulated timestamp is represented as Year-Month-Day Hour:Minute.
# Earliest reading: 
print("\nEarliest reading:") 
print(df["Time"].min())

# Latest reading:
print("\nLatest reading:")
print(df["Time"].max())

print("\n===== DATASET INFORMATION =====")
print(f"Number of records: {len(df)}")
print(f"Time range: {df['Time'].min()} to {df['Time'].max()}")
print(f"Columns: {df.columns.tolist()}")