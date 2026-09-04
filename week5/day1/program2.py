# Program 2 – Sensor Trends 
"""
Calculate: 
• Average temperature per time period.  
• Average RPM per time period.  
• Average current per time period.
"""

import pandas as pd

print("===== SENSOR TRENDS ANALYSIS =====")

# Load the motor sensor dataset
df = pd.read_csv("week5/day1/motor_sensor_data.csv")

print("\nOriginal Data:")
print(df)

# Convert the time column into a datetime format
df["Time"] = pd.to_datetime(
    "2026-09-04 " + df["Time"], format="%Y-%m-%d %H:%M"
)

# Sort records chronologically
df = df.sort_values("Time")

print("\n===== SORTED DATA =====")
print(df.head())

# Set time as the index for resampling
df.set_index("Time", inplace=True)

# Calculate hourly averages for temperature, RPM, and current
hourly_avg = df[["Temperature", "RPM", "Current"]].resample("1h").mean()

print("\n===== HOURLY SENSOR AVERAGES =====")
# Format the output to display averages with two decimal places
print(hourly_avg.round(2))