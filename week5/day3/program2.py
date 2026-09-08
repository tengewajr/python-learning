# Program 2 – Visualize Correlations 
"""
Create a correlation heatmap using Matplotlib. 
Identify: 
• Strong positive relationships.  
• Strong negative relationships.  
• Weak relationships.  
"""

import pandas as pd
import matplotlib.pyplot as plt

print("===== SENSOR CORRELATION HEATMAP =====")

# Load the dataset
df = pd.read_csv("week5/day1/motor_sensor_data.csv")

print("\nOriginal data")
print(df)

# Select sensor columns
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

# Create heatmap
plt.figure(figsize=(12,6))

plt.imshow(
    correlation_matrix,
    cmap="coolwarm",
    vmin=-1,
    vmax=+1
)

plt.colorbar(label="Correlation Coefficient")

plt.xticks(
    range(len(correlation_matrix.columns)),
    correlation_matrix.columns,
    rotation=45
)

plt.yticks(
    range(len(correlation_matrix.columns)),
    correlation_matrix.columns
)

# Display correlation values inside cells
for i in range (len(correlation_matrix)):
    for j in range (len(correlation_matrix)):
        plt.text(
            j,
            i,
            f"{correlation_matrix.iloc[i,j]:.2f}",
            ha="center",
            va="center"
        )

plt.title("Motor Sensor Correlation Heatmap")
plt.tight_layout()
plt.show()