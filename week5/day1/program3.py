# Program 3 – Identify Changes 
"""
Find: 
• Largest temperature increase.  
• Largest RPM decrease.  
• Largest current increase. 
"""

import pandas as pd

print("===== SENSOR CHANGE ANALYSIS =====")

# Load the motor sensor dataset
df = pd.read_csv("week5/day1/motor_sensor_data.csv")

print("\nOriginal Data:")   
print(df)

# Convert the time column into a datetime format
df["Time"] = pd.to_datetime(
    "2026-09-04 " + df["Time"], format="%Y-%m-%d %H:%M"
)

# Sort records chronologically
df = df.sort_values("Time").reset_index(drop=True)

print("\n===== SORTED DATA =====")
print(df.head())

print("\n===== DATASET INFORMATION =====")
print(f"Number of records: {len(df)}")

# Calculate the differences between consecutive readings
df["Temp_Change"] = df["Temperature"].diff()
df["RPM_Change"] = df["RPM"].diff()
df["Current_Change"] = df["Current"].diff()

# Find the largest temperature increase
temp_idx = df["Temp_Change"].idxmax() # Find the index of the maximum temperature change
largest_temp_increase = df.loc[temp_idx, "Temp_Change"] # Get the largest temperature increase value

# Find the largest RPM decrease
rpm_idx = df["RPM_Change"].idxmin() # Find the index of the minimum RPM change
largest_rpm_decrease = df.loc[rpm_idx, "RPM_Change"] # Get the largest RPM decrease value

# Find the largest current increase
current_idx = df["Current_Change"].idxmax() # Find the index of the maximum current change
largest_current_increase = df.loc[current_idx, "Current_Change"] # Get the largest current increase value

print("\n===== LARGEST SENSOR CHANGES =====")
print("-"*30)

print(
    f"\nLargest Temperature Increase: "
    f"{largest_temp_increase:.2f}"
)
print(f"Occurred at: {df.loc[temp_idx, 'Time']}")

print(
    f"\nLargest RPM Decrease: "
    f"{abs(largest_rpm_decrease):.2f}"
)
print(f"Occurred at: {df.loc[rpm_idx, 'Time']}")

print(
    f"\nLargest Current Increase: "
    f"{largest_current_increase:.2f}"
)
print(f"Occurred at: {df.loc[current_idx, 'Time']}")
