#Program 3 – Summary
"""
Read the CSV file and display:
    •  Highest Temperature
    •  Lowest Temperature
    •  Average Temperature
"""
import csv

print("===== MOTOR SENSOR DATA SUMMARY =====")

temperatures = []

with open("motor_sensor_data.csv", "r") as file:
    reader = csv.DictReader(file) 
    """read the CSV file as a dictionary, 
    where each row is represented as a dictionary with column headers as keys."""

    for row in reader:    
        temperature = float(row["Temperature"])
        temperatures.append(temperature)

highest_temp = max(temperatures)
lowest_temp = min(temperatures)
average_temp = sum(temperatures) / len(temperatures)

print(f"Highest Temperature: {highest_temp:.2f} C")
print(f"Lowest Temperature: {lowest_temp:.2f} C")
print(f"Average Temperature: {average_temp:.2f} C")