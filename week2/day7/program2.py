#Program 2 – Find High Current
"""Find all records where:
Current > 9

Display the records.
"""

print("===== HIGH CURRENT RECORDS =====")

import pandas as pd

df=pd.read_csv("week2/day6/motor_data.csv")
print(df)

#Then find and display all records where Current > 9
high_current_records = df[df['Current'] > 9]

print("====HIGH CURRENT RECORDS====")
print(high_current_records)