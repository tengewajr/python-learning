# Creating a Prediction Target
"""
The program should: 
1. Load the motor dataset.  
2. Sort the data by time.  
3. Identify failure events.  
4. Create a failure_soon target.  
5. Save the processed dataset.  
"""

import pandas as pd

print("===== CREATING FAILURE-SOON TARGET =====")

# Load AI4I Dataset
df = pd.read_csv("week4/day1/ai4i2020.csv")

print("\nOriginal Data")
# print(df.to_string(index=True)) // If you want to print all the data values without ...
print(df)

# Sort by UDI
df = df.sort_values("UDI").reset_index(drop=True)

print(f"\nTotal Records: {len(df)}")

# -----------------------------------------------
# Prediction window
# -----------------------------------------------

future_window = 5
print (f"Prediction Window: next {future_window} records")

# -----------------------------------------------
# Create a Failure_Soon target
# -----------------------------------------------

df["Failure_Soon"] = 0

for i in range(len(df)):

    # Determine the future records to inspect
    start = i + 1
    end = min(i + 1 + future_window, len(df))

    future_records = df.loc[start:end-1,"Machine failure"]

    # If any future record contains a failure, 
    # Mark the current record as Failure_Soon = 1
    if (future_records == 1).any():
        df.loc[i, "Failure_Soon"] = 1

# -----------------------------------------------
# Remove rows where the complete future window
# is not available
# -----------------------------------------------
df =df.iloc[:-future_window].copy()

# -----------------------------------------------
# Display results
# -----------------------------------------------

print("\n===== FAILURE-SOON SUMMARY =====")

print("Failure_Soon = 1:", (df["Failure_Soon"] == 1).sum())
print("Failure_Soon = 0:", (df["Failure_Soon"] == 0).sum())
print(f"Failure_Soon Rate: {df["Failure_Soon"].mean()*100:.2f}%")

print("\n===== EXAMPLE FAILURE SOON TARGETS =====")
print(
    df[
        [
        "UDI",
        "Air temperature [K]",
        "Process temperature [K]",
        "Rotational speed [rpm]",
        "Torque [Nm]",
        "Tool wear [min]",
        "Machine failure",
        "Failure_Soon"
        ]        
    ].head(20)
)

# -----------------------------------------------
# Save processed dataset
# -----------------------------------------------

output_file = ("week6/day2/processed_motor_data.csv")

df.to_csv(
    output_file, 
    index=False
)

print("\nProcessed dataset saved to:")
print(output_file)

# -----------------------------------------------
# Important limitation
# -----------------------------------------------

print("\n===== TARGET EXAMPLE AROUND FIRST FAILURE =====")

print(
    df[
        [
            "UDI",
            "Machine failure",
            "Failure_Soon"
        ]
    ].loc[40:55].to_string(index=False)
)

print("\n===== TARGET CONSTRUCTION EXPLANATION =====")

print(
    "For UDI 46, the next five records are 47-51, "
    "and UDI 51 is a failure. Therefore, "
    "UDI 46 is labeled Failure_Soon = 1."
)

print(
    "For UDI 51, the next five records are 52-56, "
    "and no failure occurs in that window. Therefore, "
    "UDI 51 is labeled Failure_Soon = 0."
)

print("\n===== IMPORTANT LIMITATION =====")

print(
    "The AI4I dataset has no timestamped longitudinal "
    "records for individual motors. Therefore, the "
    "5-record future window is a simplified UDI-order "
    "proxy for this learning exercise and does not "
    "represent a real 5-time-unit prediction window."
)
