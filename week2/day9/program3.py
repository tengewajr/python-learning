# Program 3 – Motor Health Status
"""Create a simple health classification:
NORMAL 
WARNING 
CRITICAL

For example:

NORMAL
→ All sensor readings are within expected range.

WARNING
→ One sensor is outside the normal range.

CRITICAL
→ Multiple sensors are outside the normal range.

"""

import pandas as pd

print("==== MOTOR HEALTH STATUS ==== ")

df=pd.read_csv("week2/day6/motor_data.csv")

# Thresholds selected for this exercise only.
# They are not scientifically validated motor safety limits.
high_temp = df["Temperature"] > 70 
high_current = df["Current"] > 9.5
low_rpm = df["RPM"] < 1450

# Identifying records that violate these thresholds. 
for _, row in df.iterrows():
    if row["Temperature"] <= 70 and row["Current"] <= 9.5 and row["RPM"] >= 1450:
        print (
            f"NORMAL | Time: {row["Time"]} | "
            f"Temperature: {row['Temperature']:.2f} | "
            f"Current: {row['Current']:.2f} | "
            f"RPM: {row['RPM']:.0f} | "
            f"Status: All sensor readings are within expected range"
        )

    if row["Temperature"] <= 70 and row["Current"] <= 9.5 and row["RPM"] < 1450:
        print(
            f"WARNING | Time: {row["Time"]} | "
            f"Temperature: {row['Temperature']:.2f} | "
            f"Current: {row['Current']:.2f} | "
            f"RPM: {row['RPM']:.0f} | "
            f"Status: RPM IS LOW; One sensor is outside the normal range."
        )

   
    if row["Temperature"] <= 70 and row["Current"] > 9.5 and row["RPM"] >= 1450:
        print(
            f"WARNING | Time: {row["Time"]} | "
            f"Temperature: {row['Temperature']:.2f} | "
            f"Current: {row['Current']:.2f} | "
            f"RPM: {row['RPM']:.0f} | "
            f"Status: CURRENT IS HIGH; One sensor is outside the normal range."
        )

    if row["Temperature"] > 70 and row["Current"] <= 9.5 and row["RPM"] >= 1450:
        print(
            f"WARNING | Time: {row["Time"]} | "
            f"Temperature: {row['Temperature']:.2f} | "
            f"Current: {row['Current']:.2f} | "
            f"RPM: {row['RPM']:.0f} | "
            f"Status: TEMPERATURE IS HIGH; One sensor is outside the normal range."
        )

    if row["Temperature"] <= 70 and row["Current"] > 9.5 and row["RPM"] < 1450:
        print(
            f"CRITICAL | Time: {row["Time"]} | "
            f"Temperature: {row['Temperature']:.2f} | "
            f"Current: {row['Current']:.2f} | "
            f"RPM: {row['RPM']:.0f} | "
            f"Status: CURRENT IS HIGH and RPM IS LOW; Multiple sensors are outside the normal range."
        )

    if row["Temperature"] > 70 and row["Current"] <= 9.5 and row["RPM"] < 1450:
        print(
            f"CRITICAL | Time: {row["Time"]} | "
            f"Temperature: {row['Temperature']:.2f} | "
            f"Current: {row['Current']:.2f} | "
            f"RPM: {row['RPM']:.0f} | "
            f"Status: TEMPERATURE IS HIGH and RPM IS LOW; Multiple sensors are outside the normal range."
        )

        if row["Temperature"] > 70 and row["Current"] > 9.5 and row["RPM"] >= 1450:
            print(
            f"CRITICAL | Time: {row["Time"]} | "
            f"Temperature: {row['Temperature']:.2f} | "
            f"Current: {row['Current']:.2f} | "
            f"RPM: {row['RPM']:.0f} | "
            f"Status: TEMPERATURE AND CURRENT ARE HIGH; Multiple sensors are outside the normal range."
        )

        if row["Temperature"] > 70 and row["Current"] > 9.5 and row["RPM"] < 1450:
                print(
                f"CRITICAL | Time: {row["Time"]} | "
                f"Temperature: {row['Temperature']:.2f} | "
                f"Current: {row['Current']:.2f} | "
                f"RPM: {row['RPM']:.0f} | "
                f"Status: RPM IS LOW WHILE TEMPERATURE AND CURRENT ARE HIGH; Multiple sensors are outside the normal range."
            )