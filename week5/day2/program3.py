# Program 3 – Identify Up Trends 
"""Try to identify periods where: 
• Temperature is Up.  
• RPM is Down.  
• Current is Up.
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

print("===== SENSOR CHANGE IDENTIFICATION =====")

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

# Calculate changes between consecutive readings for Temperature, RPM, and Current
df["Temperature_Change"] = df["Temperature"].diff()
df["RPM_Change"] = df["RPM"].diff()
df["Current_Change"] = df["Current"].diff()

# Identify periods of Up/Down trends
df["Temperature_Up"] = df["Temperature_Change"] > 0
df["RPM_Down"] = df["RPM_Change"] < 0
df["Current_Up"] = df["Current_Change"] > 0

print("\n===== SENSOR CHANGE SUMMARY =====")
print("-"*50)

print(
    "Temperature Increased in",
    df["Temperature_Up"].sum(),
    "transitions out of",
    len(df)
)

print(
    "RPM Decreased in",
    df["RPM_Down"].sum(),
    "transitions out of", 
    len(df)
)

print(
    "Current Increased in",
    df["Current_Up"].sum(),
    "transitions out of",
    len(df)
)

print("\n===== SIMULTANEOUS SENSOR CHANGES =====")
print("-"*50)

# Identify readings where Temperature is Up, RPM is Down, and Current is Up
simultaneous_Changes = df[
    (df["Temperature_Up"]) & df["RPM_Down"] & df["Current_Up"]
]

print(
    "Number of transitions where Temperature increased, "
    "RPM decreased, and Current increased:",
    len(simultaneous_Changes)
)

# Display examples
results = simultaneous_Changes[
    [
        "Time", "Temperature", "RPM", "Current",
        "Temperature_Change", "RPM_Change", "Current_Change"
    ]
].head(10).copy()

# Round only the numeric columns to two decimal places for better readability.
results[
    [
        "Temperature", "RPM", "Current",
        "Temperature_Change", "RPM_Change", "Current_Change"
    ]
] = results[
    [
        "Temperature", "RPM", "Current",
        "Temperature_Change", "RPM_Change", "Current_Change"
    ]
].round(2)

print("\nExamples of simultaneous sensor changes:")
print(results)
