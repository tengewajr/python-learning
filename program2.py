# Program 2 – Study a Failure 
"""
Choose one failure case and inspect records immediately preceding it
in UDI order.

Important:
The AI4I dataset does not provide a timestamped sequence for an
individual motor. Therefore, UDI "Unique Device Identifier" order 
is used only as a dataset sequence for this exercise, not as actual time.
"""

import pandas as pd

print("===== STUDYING ONE MOTOR FAILURE =====")
# Load the AI4I Motor dataset
df = pd.read_csv("week4/day1/ai4i2020.csv")

print("\nOriginal Data")
print(df)

# Sort by UDI
df = df.sort_values("UDI").reset_index(drop=True)

# Find the first failure case
failure_index = df.index[df["Machine failure"] == 1][0]

failure_row = df.loc[failure_index]

print("\n===== SELECTED FAILURE =====")

print("UDI:", failure_row["UDI"])
print("Type:", failure_row["Type"])
print("Air Temperature [K]:",failure_row["Air temperature [K]"])
print("Process Temperature [K]:",failure_row["Process temperature [K]"])
print("Rotational Speed [rpm]:",failure_row["Rotational speed [rpm]"])
print("Torque [Nm]:",failure_row["Torque [Nm]"])
print("Tool Wear [min]:",failure_row["Tool wear [min]"])
print("Machine Failure:",failure_row["Machine failure"])

# Get five records immediately preceding the selected failure
start_index = max(0, failure_index - 5)

previous_records = df.loc[start_index:failure_index] 

print("\n===== FAILURE AND IMMEDIATELY PRECEDING "
      "RECORDS IN UDI ORDER =====")

print(previous_records[
    [
        "UDI",
        "Type",
        "Air temperature [K]",
        "Process temperature [K]",
        "Rotational speed [rpm]",
        "Torque [Nm]",
        "Tool wear [min]",
        "Machine failure"
    ]
].to_string(index=False)
)

print("\n===== IMPORTANT LIMITATION =====")
print(
    "UDI order is used as a dataset sequence only. "
    "It is not a timestamp and does not prove that these "
    "records are successive readings from the same motor."
)