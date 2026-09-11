# Week 5 Final Mini Project
# Motor Behavior Analysis

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

print("==============================================")
print("       MOTOR BEHAVIOR ANALYSIS")
print("==============================================")

# ==================================================
# 1. LOAD DATA
# ==================================================

df = pd.read_csv(
    "week5/day1/motor_sensor_data.csv"
)

print("\n===== DATA LOADED =====")
print("Records:", len(df))
print("Columns:", df.columns.tolist())

# ==================================================
# 2. CLEAN DATA
# ==================================================

print("\n===== DATA CLEANING =====")

print("Missing values before cleaning:")
print(df.isnull().sum())

df = df.dropna()

print("\nRecords after cleaning:", len(df))

# ==================================================
# 3. SORT BY TIME
# ==================================================

df["Time"] = pd.to_datetime(
    "2026-09-10 " + df["Time"],
    format="%Y-%m-%d %H:%M"
)

df = df.sort_values("Time").reset_index(drop=True)

# ==================================================
# 4. SENSOR TREND FEATURES
# ==================================================

df["Temperature_Change"] = (
    df["Temperature"].diff()
)

df["RPM_Change"] = (
    df["RPM"].diff()
)

df["Rolling_Temperature"] = (
    df["Temperature"].rolling(window=5).mean()
)

df["Rolling_Current"] = (
    df["Current"].rolling(window=5).mean()
)

# ==================================================
# 5. ANOMALY DETECTION
# ==================================================

temperature_threshold = 75
rpm_threshold = 1420
current_threshold = 9.5

df["Temperature_Anomaly"] = (
    df["Temperature"] > temperature_threshold
)

df["RPM_Anomaly"] = (
    df["RPM"] < rpm_threshold
)

df["Current_Anomaly"] = (
    df["Current"] > current_threshold
)

df["Anomaly"] = (
    df["Temperature_Anomaly"]
    | df["RPM_Anomaly"]
    | df["Current_Anomaly"]
).astype(int)

# ==================================================
# 6. CORRELATION ANALYSIS
# ==================================================

sensor_data = df[
    [
        "Temperature",
        "Voltage",
        "Current",
        "RPM"
    ]
]

correlation_matrix = sensor_data.corr()

print("\n===== SENSOR CORRELATION =====")
print(correlation_matrix.round(2))

# ==================================================
# 7. SUMMARY
# ==================================================

print("\n===== MOTOR BEHAVIOR SUMMARY =====")

print(
    "Average Temperature:",
    round(df["Temperature"].mean(), 2)
)

print(
    "Average Current:",
    round(df["Current"].mean(), 2)
)

print(
    "Average RPM:",
    round(df["RPM"].mean(), 2)
)

print(
    "Potential anomalous readings:",
    df["Anomaly"].sum()
)

# ==================================================
# 8. ENGINEERED FEATURES
# ==================================================

print("\n===== ENGINEERED FEATURES =====")

display_data = df[
    [
        "Time",
        "Temperature",
        "Temperature_Change",
        "RPM",
        "RPM_Change",
        "Rolling_Temperature",
        "Rolling_Current",
        "Anomaly"
    ]
].head(10).copy()

numeric_columns = [
    "Temperature",
    "Temperature_Change",
    "RPM",
    "RPM_Change",
    "Rolling_Temperature",
    "Rolling_Current"
]

display_data[numeric_columns] = (
    display_data[numeric_columns].round(2)
)

print(display_data)

# ==================================================
# 9. GRAPH 1 — TEMPERATURE OVER TIME
# ==================================================

fig, ax = plt.subplots(figsize=(12, 5))

ax.plot(
    df["Time"],
    df["Temperature"],
    label="Temperature"
)

ax.plot(
    df["Time"],
    df["Rolling_Temperature"],
    label="5-Reading Rolling Average",
    linewidth=2
)

ax.xaxis.set_major_locator(
    mdates.MinuteLocator(interval=15)
)

ax.xaxis.set_major_formatter(
    mdates.DateFormatter("%H:%M")
)

ax.set_title("Temperature Over Time")
ax.set_xlabel("Time")
ax.set_ylabel("Temperature")
ax.legend()
ax.grid()

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# ==================================================
# 10. GRAPH 2 — RPM OVER TIME
# ==================================================

fig, ax = plt.subplots(figsize=(12, 5))

ax.plot(
    df["Time"],
    df["RPM"],
    label="RPM"
)

ax.xaxis.set_major_locator(
    mdates.MinuteLocator(interval=15)
)

ax.xaxis.set_major_formatter(
    mdates.DateFormatter("%H:%M")
)

ax.set_title("RPM Over Time")
ax.set_xlabel("Time")
ax.set_ylabel("RPM")
ax.legend()
ax.grid()

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# ==================================================
# 11. GRAPH 3 — CURRENT OVER TIME
# ==================================================

fig, ax = plt.subplots(figsize=(12, 5))

ax.plot(
    df["Time"],
    df["Current"],
    label="Current"
)

ax.plot(
    df["Time"],
    df["Rolling_Current"],
    label="5-Reading Rolling Average",
    linewidth=2
)

ax.xaxis.set_major_locator(
    mdates.MinuteLocator(interval=15)
)

ax.xaxis.set_major_formatter(
    mdates.DateFormatter("%H:%M")
)

ax.set_title("Current Over Time")
ax.set_xlabel("Time")
ax.set_ylabel("Current")
ax.legend()
ax.grid()

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# ==================================================
# 12. GRAPH 4 — SENSOR CORRELATION
# ==================================================

plt.figure(figsize=(8, 6))

plt.imshow(
    correlation_matrix,
    cmap="coolwarm",
    vmin=-1,
    vmax=1
)

plt.colorbar(
    label="Correlation Coefficient"
)

plt.xticks(
    range(len(correlation_matrix.columns)),
    correlation_matrix.columns,
    rotation=45
)

plt.yticks(
    range(len(correlation_matrix.columns)),
    correlation_matrix.columns
)

for i in range(len(correlation_matrix)):
    for j in range(len(correlation_matrix)):
        plt.text(
            j,
            i,
            f"{correlation_matrix.iloc[i, j]:.2f}",
            ha="center",
            va="center"
        )

plt.title("Motor Sensor Correlation")
plt.tight_layout()
plt.show()

# ==================================================
# 13. GRAPH 5 — ANOMALIES OVER TIME
# ==================================================

fig, ax = plt.subplots(figsize=(12, 5))

ax.plot(
    df["Time"],
    df["Temperature"],
    label="Temperature"
)

anomaly_data = df[
    df["Anomaly"] == 1
]

ax.scatter(
    anomaly_data["Time"],
    anomaly_data["Temperature"],
    marker="x",
    s=70,
    label="Potential Anomaly"
)

ax.xaxis.set_major_locator(
    mdates.MinuteLocator(interval=15)
)

ax.xaxis.set_major_formatter(
    mdates.DateFormatter("%H:%M")
)

ax.set_title(
    "Motor Temperature and Potential Anomalies"
)

ax.set_xlabel("Time")
ax.set_ylabel("Temperature")
ax.legend()
ax.grid()

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

print("\n==============================================")
print("       MOTOR BEHAVIOR ANALYSIS COMPLETE")
print("==============================================")
