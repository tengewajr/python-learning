#Program 2 – Identify Abnormal Readings
"""Create rules for identifying potentially abnormal readings. 
For example:
Temperature > 75 → HIGH TEMPERATURE 
Current > 10 → HIGH CURRENT
RPM < 1400 → LOW RPM

The program should identify records that violate these thresholds. 

Example:

WARNING

Time: 09:42
Temperature: 78.4
Status: HIGH TEMPERATURE
"""

import pandas as pd

print("==== ABNORMAL READINGS ==== ")

df=pd.read_csv("week2/day6/motor_data.csv")

"""
# Define Terms Condition
# Thresholds selected for this exercise only.
# They are not scientifically validated motor safety limits.
high_temp = df["Temperature"] > 70  #produces True/False values
high_current = df["Current"] > 9.5
low_rpm = df["RPM"] < 1450

abnormal_records=df[high_temp | high_current | low_rpm]
"""

# Identifying records that violate these thresholds. 
for _, row in df.iterrows():
    if row["Temperature"] >70:
        print (
            f"WARNING | Time: {row['Time']} | "
            f"Temperature: {row['Temperature']:.2f} | "
            f"Status: HIGH TEMPERATURE"
        )

    if row["Current"] > 9.5:
        print(
            f"WARNING | Time: {row['Time']} | "
            f"Current: {row['Current']:.2f} | "
            f"Status: HIGH CURRENT"
        )

    if row["RPM"] < 1450:
        print(
            f"WARNING | Time: {row['Time']} | "
            f"RPM: {row['RPM']:.0f} | "
            f"Status: LOW RPM"
        )