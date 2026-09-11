# Program 1 – Feature Engineering
"""
Create new features from raw motor sensor data:

1. Temperature Change
2. RPM Change
3. Rolling Temperature
4. Rolling Current
5. Anomaly Flag
"""

import pandas as pd

print("===== MOTOR FEATURE ENGINEERING =====")

# Load dataset
df = pd.read_csv(
    "week5/day1/motor_sensor_data.csv"
)

# Convert Time to datetime
df["Time"] = pd.to_datetime(
    "2026-09-10 " + df["Time"],
    format="%Y-%m-%d %H:%M"
)

# Sort chronologically
df = df.sort_values("Time").reset_index(drop=True)

# ------------------------------------------------
# Feature 1: Temperature Change
# ------------------------------------------------

df["Temperature_Change"] = (
    df["Temperature"].diff()
)

# ------------------------------------------------
# Feature 2: RPM Change
# ------------------------------------------------

df["RPM_Change"] = (
    df["RPM"].diff()
)

# ------------------------------------------------
# Feature 3: 5-reading Rolling Temperature
# ------------------------------------------------

df["Rolling_Temperature"] = (
    df["Temperature"].rolling(window=5).mean()
)

# ------------------------------------------------
# Feature 4: 5-reading Rolling Current
# ------------------------------------------------

df["Rolling_Current"] = (
    df["Current"].rolling(window=5).mean()
)

# ------------------------------------------------
# Feature 5: Anomaly Flag
# Learning thresholds from Day 4
# ------------------------------------------------

temperature_threshold = 75
rpm_threshold = 1420
current_threshold = 9.5

df["Temperature_Anomaly"] = (
    df["Temperature"] > temperature_threshold
)

df["RPM_Anomaly"] = (
    df["RPM"] < rpm_threshold
)

df["Current_Anomaly"] = (
    df["Current"] > current_threshold
)

df["Anomaly"] = (
    df["Temperature_Anomaly"]
    | df["RPM_Anomaly"]
    | df["Current_Anomaly"]
).astype(int)

# ------------------------------------------------
# Display engineered features
# ------------------------------------------------

print("\n===== ENGINEERED FEATURES =====")

print(
    df[
        [
            "Time",
            "Temperature",
            "Temperature_Change",
            "RPM",
            "RPM_Change",
            "Current",
            "Rolling_Temperature",
            "Rolling_Current",
            "Anomaly"
        ]
    ].head(10)
)

print("\n===== FEATURE INFORMATION =====")

print(
    df[
        [
            "Temperature_Change",
            "RPM_Change",
            "Rolling_Temperature",
            "Rolling_Current",
            "Anomaly"
        ]
    ].describe().round(2)
)