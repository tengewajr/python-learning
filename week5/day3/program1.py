# Program 1 – Correlation Matrix 
""" 
Using Pandas, calculate the correlation between: 
• Temperature  
• Voltage  
• Current  
• RPM  
• Torque  
• Vibration  
Only use columns that actually exist in his dataset. 
(Since Torque and Vibration are not in the dataset, they will be ignored.)
"""

import pandas as pd

print("===== SENSOR CORRELATION ANALYSIS =====")

# Load the dataset
df = pd.read_csv("week5/day1/motor_sensor_data.csv")

print("\nOriginal data")
print(df)

# Select numerical columns
sensor_data = df [
    [
        "Temperature",
        "Voltage",
        "Current",
        "RPM"
    ]
]

# Calculate correlation matrix
correlation_matrix = sensor_data.corr()

print("\n===== CORRELATION MATRIX =====")
print(correlation_matrix.round(2))