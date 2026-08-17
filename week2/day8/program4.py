#Program 4 – Compare Two Sensors.
"""Create a graph comparing two measurements. 
For example:
- Temperature 
- Current

over time.
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

print("==== COMPARING TWO SENSORS ====")

# Read Original dataset
df=pd.read_csv("week2\day6\motor_data.csv")

# Converting Time from string to datetime
df["Time"]=pd.to_datetime(df["Time"],format="%H:%M")

# Create figure and first axis
fig, ax1=plt.subplots(figsize=(12,6))

# Plot Temperature
line1 = ax1.plot(
    df["Time"],
    df["Temperature"],
    label="Temperature",
    color="blue",
    marker=".",
    linewidth=2
)

ax1.set_xlabel("Time")
ax1.set_ylabel("Temperature (°C)")

# Create a second Y-axis
ax2=ax1.twinx()

# Plot Current
line2 = ax2.plot(
    df["Time"],
    df["Current"],
    label="Current",  
    color="green",
    marker="*",
    linewidth=2
)

ax2.set_ylabel("Current (A)")

# Title
plt.title("Motor Temperature and Current Over Time")

#Format X-axis
ax1.xaxis.set_major_locator(
    mdates.MinuteLocator(interval=10)
)

ax1.xaxis.set_major_formatter(
    mdates.DateFormatter("%H:%M")
)

# Rotate time labels
plt.setp(
    ax1.get_xticklabels(),
    rotation=45    
)

# Combine Legends from both axes
lines = line1 + line2
labels = [line.get_label() for line in lines]

ax1.legend(lines, labels, loc=("upper right"))

# Add grid
ax1.grid(
    which="both", 
    linewidth=0.5, 
    linestyle="--"
)

# Adjust layout
fig.tight_layout()

# Save figure
fig.savefig(
    "week2/day8/temperature_and_current_over_time.png"
)

# Display graph
plt.show()