#Program 3 – Sort the Data
"""Sort the motor data by:
•	Temperature
•	Current
•	RPM
Try both ascending and descending order.
"""

print("===== SORT MOTOR SENSOR DATA =====")
import pandas as pd

df=pd.read_csv("week2/day6/motor_data.csv")
print("Original Data:")
print(df)

# Sort by Temperature (ascending)
print("\nSorted by Temperature (Ascending):")
print(df.sort_values("Temperature"))

# Sort by Temperature (descending)
print("\nSorted by Temperature (Descending):")
print(df.sort_values("Temperature", ascending=False))

# Sort by Current (ascending)
print("\nSorted by Current (Ascending):")
print(df.sort_values("Current"))

# Sort by Current (descending)
print("\nSorted by Current (Descending):")
print(df.sort_values("Current", ascending=False))

# Sort by RPM (ascending)
print("\nSorted by RPM (Ascending):")
print(df.sort_values("RPM"))

# Sort by RPM (descending)
print("\nSorted by RPM (Descending):")
print(df.sort_values("RPM", ascending=False))
