#Program 3 – Current Over Time
"""Create:

Time → Current
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

print("==== MOTOR CURRENT OVER TIME ====")

#Read dataset
df=pd.read_csv("week2/day6/motor_data.csv")

#Convert time from strings to datetime
df["Time"]=pd.to_datetime(df["Time"],format="%H:%M")

#Create figure
plt.figure(figsize=(12,6))

#Plot Current
plt.plot(
df["Time"],
df["Current"],
label="Current",
color="green",
marker="*",
linewidth=2
)

#Graph Label
plt.xlabel("Time")
plt.ylabel("Current")
plt.title("Motor Current Over Time")

#Format X-Axis
plt.gca().xaxis.set_major_locator(mdates.MinuteLocator(interval=10))
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter("%H:%M"))

plt.legend()
plt.grid(which="both",linewidth=0.5, linestyle="--")

plt.tight_layout()
plt.savefig("week2/day8/motor_current_over_time.png")

plt.show()
