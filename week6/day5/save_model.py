# Day 5 - Program 1
# Train and Save the Predictive Maintenance Model

import pandas as pd
import joblib

from sklearn.ensemble import RandomForestClassifier


print("==============================================")
print("     SAVE PREDICTIVE MAINTENANCE MODEL")
print("==============================================")


# ==================================================
# 1. LOAD PROCESSED DATA
# ==================================================

df = pd.read_csv(
    "week6/day2/processed_motor_data.csv"
)

print("\n===== DATASET =====")
print("Records:", len(df))
print("Columns:", df.columns.to_list())

# ==================================================
# 2. SELECT FEATURES
# ==================================================

features = [
    "Air temperature [K]",
    "Process temperature [K]",
    "Rotational speed [rpm]",
    "Torque [Nm]",
    "Tool wear [min]"
]

X = df[features]


# ==================================================
# 3. SELECT TARGET
# ==================================================

y = df["Failure_Soon"]


# ==================================================
# 4. CHRONOLOGICAL TRAIN / TEST SPLIT
# ==================================================

split_index = int(len(df) * 0.80)

X_train = X.iloc[:split_index]
y_train = y.iloc[:split_index]


# ==================================================
# 5. TRAIN RANDOM FOREST
# ==================================================

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

print("\nModel training completed successfully!")


# ==================================================
# 6. SAVE MODEL
# ==================================================

joblib.dump(
    model,
    "week6/day5/motor_model.pkl"
)

print("\nModel saved successfully!")
print("File: week6/day5/motor_model.pkl")
