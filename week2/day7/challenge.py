#Small Challenge
"""Create a program that displays:
Motor Records Above Normal Temperature

and shows all records where the temperature exceeds your chosen threshold.
"""

print("===== MOTOR RECORDS ABOVE NORMAL TEMPERATURE =====")
import pandas as pd
df=pd.read_csv("week2/day6/motor_data.csv")

#Set the threshold temperature
threshold_temp = float(input("Enter the temperature threshold: "))

#Find and display all records where Temperature exceeds the threshold
above_normal_temp_records = df[df['Temperature'] > threshold_temp]
print("Records with Temperature above normal:")
print(above_normal_temp_records)
