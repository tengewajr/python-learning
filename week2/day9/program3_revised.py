
import pandas as pd

print("==== MOTOR HEALTH STATUS ==== ")

df=pd.read_csv("week2/day6/motor_data.csv")

# Thresholds selected for this exercise only.
# They are not scientifically validated motor safety limits.

for _, row in df.iterrows():
    high_temp = row["Temperature"] > 70 #produces 1 or 0 values
    high_current = row["Current"] > 9.5
    low_rpm = row["RPM"] < 1450

    abnormal_count=sum([high_temp, high_current, low_rpm])

    if abnormal_count == 0:
            status = "NORMAL"
            message = "All sensor readings are within expected range."

    elif abnormal_count == 1:
            status = "WARNING"
            message = "One sensor is outside the normal range."

    else:
            status = "CRITICAL"
            message = "Multiple sensors are outside the normal range."

    print(
           f"{status} |"
           f"Time: {row["Time"]} | "
           f"Temperature: {row['Temperature']:.2f} | "
           f"Current: {row['Current']:.2f} | "
           f"RPM: {row['RPM']:.0f} | "
           f"Status: {message}"     
    )
                