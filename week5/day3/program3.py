# Program 3 – Scatter Plots 
""" Choose two potentially interesting relationships. 
For example: 
Temperature vs RPM 
and 
Current vs Temperature 

Create scatter plots.
"""

import pandas as pd
import matplotlib.pyplot as plt

print("===== SENSOR SCATTER PLOTS =====")

# Load the dataset
df = pd.read_csv("week5/day1/motor_sensor_data.csv")

# Temperature Vs RPM
plt.figure(figsize=(8,5))

plt.scatter(
    df["Temperature"],
    df["RPM"]
)

plt.title("Temperature Vs RPM")
plt.xlabel("Temperature")
plt.ylabel("RPM")
plt.grid()
plt.tight_layout()
plt.show()

# Current Vs Temperature
plt.figure(figsize=(8,5))

plt.scatter(
    df["Temperature"],
    df["Current"]
)

plt.title("Temperature Vs Current")
plt.xlabel("Temperature")
plt.ylabel("Current")
plt.grid()
plt.tight_layout()
plt.show()
