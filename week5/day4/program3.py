# Program 3 – Create an Anomaly Column 
"""
Add a new column: Anomaly 

Anomaly = 0 -> Normal
Anomaly = 1 -> Potential Anomaly

Visualization - Create a graph showing: 
• Sensor readings  
• Highlighted abnormal readings  
"""

import pandas as pd

print("===== MOTOR ANOMALY CLASSIFICATION =====")

# Load the dataset
df = pd.read_csv("week5/day1/motor_sensor_data.csv")

print("\nOriginal Data")
print(df)

# Defining Learning threshold
temperature_threshold = 75
rpm_threshold = 1420
current_threshold = 9.5

# Create sensor anomaly flags
df["Temperature_Anomaly"] = (
    df["Temperature"] > temperature_threshold
)

df["RPM_Anomaly"] = (
    df["RPM"] < rpm_threshold
)

df["Current_Anomaly"] = (
    df["Current"] > current_threshold
)

# Combine all anomaly conditions
df["Anomaly"] = (
    df["Temperature_Anomaly"]
    | df["RPM_Anomaly"]
    | df["Current_Anomaly"]
).astype(int)

# Converting Time to datetime for time-series analysis
df["Time"] = pd.to_datetime(
    "2026-09-08 " + df["Time"],
    format = "%Y-%m-%d %H:%M"
)

# Sot chronologically
df = df.sort_values("Time").reset_index(drop=True)

print("\n==== ANOMALY RESULTS ====")
print("-"*40)

print(
    df[
        [
            "Time",
            "Temperature",
            "RPM",
            "Current",
            "Anomaly"
        ]
    ].head(20)
)

print("\n==== ANOMALY SUMMARY ====")
print(
    "Normal readings:",
    (df["Anomaly"] == 0).sum()
)

print(
    "Anomalous readings:",
    (df["Anomaly"] == 1).sum()
)

# ===============================================
# Save anomaly column permanently to a new CSV 
# ===============================================

output_file = "week5/day4/motor_sensor_data_with_anomaly.csv"

df.to_csv(
    output_file,
    index=False
)

print("\nSaved updated dataset to:")
print(output_file)

print("\n")
print("-"*50)
print("===== GRAPHICAL VISUALIZATION =====")
print("-"*50)

import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Create graph
fig, ax = plt.subplots(figsize=(12,6))

ax.plot(
    df["Time"],
    df["Temperature"],
    label = "Temperature"
)

# Select anomolous readings
anomaly_data = df[df["Anomaly"] == 1]

# Highligh anomalies
ax.scatter(
    anomaly_data["Time"],
    anomaly_data["Temperature"],
    marker="x",
    s=80,
    label="Anomaly"
)

# Format x-axis
ax.xaxis.set_major_locator(
    mdates.MinuteLocator(interval=15)
)
ax.xaxis.set_major_formatter(
    mdates.DateFormatter("%H:%M")
)

ax.set_title("Motor Temperature and Detected Anomalies")
ax.set_xlabel("Time")
ax.set_ylabel("Temperature")
ax.legend()
ax.grid()

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
