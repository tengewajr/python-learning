# Program 2 – Statistical Detection 
"""
Introduce the idea of: 
Mean + Standard Deviation 

Identify values that are unusually far away from the normal behavior of the dataset. 
The important idea is: 
"If most readings are around a normal range and one reading is extremely far away, 
we can flag it as potentially abnormal."
"""

import pandas as pd

print("===== STATISTICAL ANOMALY DETECTED =====")

# Load the dataset
df = pd.read_csv("week5/day1/motor_sensor_data.csv")

# Sensors to analyze
sensors = [
    "Temperature",
    "Current",
    "RPM"
]

for sensor in sensors:

    mean = df[sensor].mean()
    std = df[sensor].std()

    upper_limit = mean + (2 * std)
    lower_limit = mean - (2 * std)

    print(f"\n==== {sensor} ====")
    print("-"*30)

    print(f"Mean: {mean:.2f}")
    print(f"Standard Deviation: {std:.2f}")
    print(f"Upper Limit: {upper_limit:.2f}")
    print(f"Lower Limit: {lower_limit:.2f}")

    anomalies = df[
        (df[sensor] < lower_limit)
        | (df[sensor] > upper_limit)
    ]

    print(
        f"Potential anomalies: {len(anomalies)}"
    )