#Practical Work
#Program 1 – Motor Statistics
"""Calculate:

Temperature
• Average
• Minimum
• Maximum
• Standard deviation

Voltage
•	Average
•	Minimum
•	Maximum

Current
•	Average
•	Minimum
•	Maximum

RPM
•	Average
•	Minimum

Maximum Display something like:

MOTOR STATISTICS
-------------------------
Temperature Average: 61.4
Minimum: 55.2
Maximum: 78.1

RPM
Average: 1482.4
Minimum: 1430
Maximum: 1510
"""

import pandas as pd

print("==== MOTOR STATISTICS ====")
print ("-"*30)

df=pd.read_csv("week2/day6/motor_data.csv")

print("\n Temperature")
print(f"Average: {df["Temperature"].mean():.2f}")
print(f"Minimum: {df["Temperature"].min():.2f}")
print(f"Maximum: {df["Temperature"].max():.2f}")
print(f"Standard deviation: {df["Temperature"].std():.2f}")

print("\n Voltage")
print (f"Average: {df["Voltage"].mean():.2f}")
print (f"Maximum: {df["Voltage"].max():.2f}")
print (f"Minimum: {df["Voltage"].min():.2f}")

print("\n Current")
print(f"Average: {df["Current"].mean():.2f}")
print(f"Minimum: {df["Current"].min():.2f}")
print(f"Maximum: {df["Current"].max():.2f}")

print("\n RPM")
print(f"Average: {df["RPM"].mean():.2f}")
print(f"Minimum: {df["RPM"].min():.2f}")
print(f"Maximum: {df["RPM"].max():.2f}")




