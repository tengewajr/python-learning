#Program 2 – Motor Sensor Data Generator
"""
Generate random values for:
  • Temperature
  • Voltage
  • Current
  • RPM
Save at least 100 records into a CSV file. 
Example:
Time,Temperature,Voltage,Current,RPM 
09:00,61,415,8.2,1480
09:01,60,414,8.1,1482
09:02,62,416,8.3,1478
"""

print("===== MOTOR SENSOR DATA GENERATOR =====")

import csv
import random

with open("motor_data.csv", "w", newline="") as file:

    writer = csv.writer(file) 

    #csv header
    writer.writerow(["Time", "Temperature", "Voltage", "Current", "RPM"])

    #Generate 100 records of random values
    for i in range(100):
        hour = 9 + i // 60      #  i//  → tells us WHICH HOUR;   i // 60 → complete hours passed
        minute = i % 60         #  %  → tells us WHICH MINUTE;  i % 60  → remaining minutes
        time = f"{hour:02d}:{minute:02d}" 
        """
        It basically says.... 
        For every record, treat i as the number of minutes elapsed since 09:00, 
        calculate the corresponding hour and minute, then format it as HH:MM.
        i = 0   → 09:00
        i = 1   → 09:01
        i = 2   → 09:02
        ...
        i = 58  → 09:58
        i = 59  → 09:59
        i = 60  → 10:00
        i = 61  → 10:01
        ...
        i = 99  → 10:39
        """
        temperature = round(random.uniform(50, 80), 2)
        voltage = round(random.uniform(410, 420), 2)
        current = round(random.uniform(7, 10), 2)
        rpm = random.randint(1400, 1500)

        writer.writerow([time, temperature, voltage, current, rpm])

print("\n 100 Motor sensor data has been generated and saved to 'motor_data.csv'.")