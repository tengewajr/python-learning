#Practical Work
#Use the motor dataset.
#Program 1 – Temperature Over Time
"""Create a line graph showing: Time → Temperature

The graph should have:
•	X-axis: Time
•	Y-axis: Temperature
•	Title: Motor Temperature Over Time
"""

import pandas as pd # Import the pandas library for data manipulation and analysis
import matplotlib.pyplot as plt # Import the matplotlib library for plotting

print("===== MOTOR TEMPERATURE OVER TIME =====")

df = pd.read_csv("week2/day6/motor_data.csv") # Read the motor data from a CSV file into a pandas DataFrame

plt.figure(figsize=(12, 6)) 
#Creates a new figure with a specified size of 12 inches in width and 6 inches in height, providing ample space for the plot.

plt.plot( 
    df['Time'], 
    df['Temperature'], 
    label='Temperature', 
    color='blue',
    linewidth=2
) #Plots the temperature data against time, with a blue line of width 2 and a label for the legend.

plt.xlabel("Time")
plt.ylabel("Temperature")
plt.title("Motor Temperature Over Time")

plt.xticks(
    df.index[::10], # Show every 10th index
    df["Time"].iloc[::10], # Show every 10th time value
    rotation=45 # Rotate x-axis labels for better readability
)  # Show every 10th time label for better readability

plt.legend() # Adds a legend to the plot, which helps identify the plotted data series.
plt.grid(which='both', linestyle='--', linewidth=0.5)  # Adds a grid for both major and minor ticks with dashed lines and a thinner width.

plt.tight_layout()  # Adjust layout to prevent clipping of labels

plt.savefig("week2/day8/motor_temperature_over_time.png") #Saves the plot as a PNG file in the specified directory.
plt.show() #Displays the plot in a window. This is useful for interactive sessions where you want to visualize the data immediately.