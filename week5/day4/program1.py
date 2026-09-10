# Program 1 – Simple Threshold Detection 
"""
Create rules such as: 
Temperature > X → Temperature Anomaly 
 
RPM < Y → RPM Anomaly 
 
Current > Z → Current Anomaly 
Use appropriate thresholds for the dataset. 

Remember: 
These thresholds are for learning purposes unless they come from actual motor specifications.
"""

import pandas as pd

print("===== THRESHOLD-BASED ANOMALY DETECTION =====")

# Load the dataset
df = pd.read_csv("week5/day1/motor_sensor_data.csv")

print("\nOriginal Data")
print(df)

# Learning threshold
temperature_threshold = 75
rpm_threshold = 1420
current_threshold = 9.5

# Detect anomalies
df["Temperature_Anomaly"] = (
    df["Temperature"] > temperature_threshold
)

df["RPM_Anomaly"] = (
    df["RPM"] < rpm_threshold
)

df["Current_Anomaly"] = (
    df["Current"] > current_threshold
)

# Print total number of anomalies
print("\n==== ANOMALY SUMMARY ====")
print("-"*40)

print(
    "Temperature anomalies:",
    df["Temperature_Anomaly"].sum()
)

print(
    "RPM anomalies:",
    df["RPM_Anomaly"].sum()
)

print(
    "Current anomalies:",
    df["Current_Anomaly"].sum()
)

print("\n==== EXAMPLE ANOMALOUS READINGS ====")
print("-"*40)

anomalies=df[
    df["Temperature_Anomaly"]
    | df["RPM_Anomaly"]
    | df["Current_Anomaly"]
]

print(
    anomalies[
        [
            "Time",
            "Temperature",
            "RPM",
            "Current"
        ]
    ].head(10)
)