#Program 2 – RPM Over Time
"""Create a graph showing:

Time → RPM
"""
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates 

print("===== MOTOR RPM OVER TIME =====")

#Read dataset
df = pd.read_csv("week2/day6/motor_data.csv")

#Convert Time from strings to datetime
df["Time"]=pd.to_datetime(df["Time"],format="%H:%M")

#Create figure
plt.figure(figsize=(12, 6))

#Plot RPM
plt.plot(
    df['Time'],
    df['RPM'],
    label='RPM',
    color='red',
    marker=".",
    linewidth=2
)

#Labels and Titles
plt.xlabel("Time")
plt.ylabel("RPM")
plt.title("Motor RPM over Time")

#Format X-axis
plt.gca().xaxis.set_major_locator(mdates.MinuteLocator(interval=10))
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter("%H:%M"))

#Rotate labels
plt.xticks(rotation=45)

#Legend and grid
plt.legend()
plt.grid(True, linestyle="--", linewidth=0.5)

#Prevent overlapping elements
plt.tight_layout()

#Save graph
plt.savefig("week2/day8/motor_rpm_over_time.png")

#Display graph
plt.show()