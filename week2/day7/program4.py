#Program 4 – Missing Data
"""Check whether the dataset contains missing values. If there are missing values:
•	Identify them.
•	Decide how you would handle them.

For example:
Temperature = missing

Possible approaches:
•	Remove the record.
•	Replace it with an appropriate value.

Important: Don't just remove data without understanding why you are doing it
"""

print("===== CHECK FOR MISSING DATA =====")
import pandas as pd
df=pd.read_csv("week2/day6/motor_data.csv")
print("Original Data:")
print(df)

print("\nMissing Data Check:")
print(df.isnull().sum())