"""Continue working with: motor_data.csv

Program 1 – Find High Temperature
Find all records where:
Temperature > 70

Display those records.
"""

print("===== HIGH TEMPERATURE RECORDS =====")

import pandas as pd

#Read the motor_data.csv file into a DataFrame
df=pd.read_csv("week2/day6/motor_data.csv")
print(df)

#Then find and display all records where Temperature > 70
high_temp_records = df[df['Temperature'] > 70]

print("====HIGH TEMPERATURE RECORDS====")
print(high_temp_records)