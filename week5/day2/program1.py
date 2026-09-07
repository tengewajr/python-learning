# Program 1 – Temperature Trend 
"""
Create a graph containing: 
• Original temperature  
• Rolling average temperature  
The purpose is to visually compare: Raw sensor data vs smoothed sensor data. 
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

print("===== TEMPERATURE TREND ANALYSIS =====")

# Load the motor sensor dataset
df= pd.read_csv("week5/day1/motor_sensor_data.csv")

print("\nOriginal Data:")
print(df)

# Convert the time column into a datetime format
df["Time"] = pd.to_datetime(
    "2026-09-07 " + df["Time"], 
    format="%Y-%m-%d %H:%M"
)

# Sort records chronologically
df = df.sort_values("Time").reset_index(drop=True)

# Calculate the 5-reading rolling average for the temperature column
df["Rolling_Avg_Temperature"] = (
    df["Temperature"].rolling(window=5).mean()
)

print("\n===== TEMPERATURE TREND DATA =====")

# Display the first 10 records.
display_data = df[
    [
        "Time", 
        "Temperature", 
        "Rolling_Avg_Temperature"
    ]
].head(10).copy()

# Round only the numeric columns to two decimal places for better readability.
display_data[
    [
        "Temperature", 
        "Rolling_Avg_Temperature"
        ]
] = display_data[
    [
        "Temperature", 
        "Rolling_Avg_Temperature"
    ]
].round(2)

print(display_data)

# Create the figure
fig, ax = plt.subplots(figsize=(12, 6))

# Plot the original (raw) temperature
ax.plot(
    df["Time"], 
    df["Temperature"], 
    label="Original Temperature",
    marker="o",
    linewidth=1
)

# Plot the rolling average temperature
ax.plot(
    df["Time"], 
    df["Rolling_Avg_Temperature"], 
    label="5-Reading Rolling Average",
    marker="*", 
    linewidth=2
)

# Customize the x-axis to show time in HH:MM format with 15-minute intervals
ax.xaxis.set_major_locator(
    mdates.MinuteLocator(interval=15)
)

ax.xaxis.set_major_formatter(
    mdates.DateFormatter("%H:%M")
)

# Add labels, title, legend, and grid to the plot

# ax.set_title("") = plt.title("") => set the title of the graph
ax.set_title("Temperature: Raw vs Rolling Average") 

ax.set_xlabel("Time")
ax.set_ylabel("Temperature")
ax.legend() # Show the legend
ax.grid() # Show grid lines for better readability
ax.set_xticks(df["Time"][::15])  # Set x-ticks at 15-minute intervals
plt.xticks(rotation=45) # Rotate x-tick labels for better readability
plt.tight_layout() # Adjust layout to prevent clipping of tick-labels

plt.show() # Display the plot
