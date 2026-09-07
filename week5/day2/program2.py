# Program 2 – RPM Trend 
"""
Create a graph containing: 
• Original RPM 
• Rolling average RPM 
The purpose is to visually compare: Raw sensor data vs smoothed sensor data. 
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

print("===== RPM TREND ANALYSIS =====")

# Load Motor sensor dataset
df=pd.read_csv("week5/day1/motor_sensor_data.csv")
print("\nOriginal Data:")
print(df)

# Convert the time column into datetime format
df["Time"]=pd.to_datetime(
    "2026-09-07 " + df["Time"],
    format="%Y-%m-%d %H:%M"
)

# Sort records chronologically
df = df.sort_values("Time").reset_index(drop=True)

# Calculate the 5-reading rolling average for the RPM column
df ["Rolling_avg_RPM"] = (
    df["RPM"].rolling(window=5).mean()
)

print("\n===== RPM TREND DATA =====")

# Display the first 10 records
display_data = df[
    [
        "Time",
        "RPM",
        "Rolling_avg_RPM"
    ]
].head(10).copy()

# Round only the numeric columns to two decimal places for better readability.
display_data[
    [
        "RPM",
        "Rolling_avg_RPM"
    ]
] = display_data[
    [
        "RPM",
        "Rolling_avg_RPM"
    ]
].round(2)

print(display_data)

# Create the fig
fig, ax = plt.subplots(figsize=(12, 6))

# Plot the original (raw) RPM
ax.plot(
    df["Time"],
    df["RPM"],
    label="Original RPM",
    marker="o",
    linewidth=1
)

# Plot the rolling average RPM
ax.plot(
    df["Time"],
    df["Rolling_avg_RPM"],
    label="Rolling Average RPM",
    marker="*",
    linewidth=2
)

# Set the x-axis major ticks to every 15 minutes
ax.xaxis.set_major_locator(
    mdates.MinuteLocator(interval=15)
)
ax.xaxis.set_major_formatter(
    mdates.DateFormatter("%H:%M")
)

# Set the x-axis label, y-axis label, and title of the graph
ax.set_xlabel("Time")
ax.set_ylabel("RPM")
ax.set_title("RPM Trend Analysis: Raw vs Rolling Average")
ax.legend()
ax.grid()

ax.set_xticks(df["Time"][::15])  # Set x-ticks at 15-minute intervals
plt.xticks(rotation=45) # Rotate x-tick labels for better readability
plt.tight_layout() 

# Show the graph
plt.show()