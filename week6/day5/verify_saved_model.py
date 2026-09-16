# Day 5 - Program 5
# Verify Saved Model Against Known Test Record

import joblib
import pandas as pd


print("==============================================")
print("       VERIFY SAVED MODEL PREDICTION")
print("==============================================")


# ==================================================
# 1. LOAD DATA AND SAVED MODEL
# ==================================================

df = pd.read_csv(
    "week6/day2/processed_motor_data.csv"
)

model = joblib.load(
    "week6/day5/motor_model.pkl"
)


# ==================================================
# 2. FIND UDI 8013
# ==================================================

record = df[df["UDI"] == 8013].copy()

print("\n===== ORIGINAL RECORD =====")
print(
    record[
        [
            "UDI",
            "Air temperature [K]",
            "Process temperature [K]",
            "Rotational speed [rpm]",
            "Torque [Nm]",
            "Tool wear [min]",
            "Failure_Soon"
        ]
    ].to_string(index=False)
)


# ==================================================
# 3. SELECT FEATURES
# ==================================================

features = [
    "Air temperature [K]",
    "Process temperature [K]",
    "Rotational speed [rpm]",
    "Torque [Nm]",
    "Tool wear [min]"
]

X_record = record[features]


# ==================================================
# 4. PREDICT USING SAVED MODEL
# ==================================================

prediction = model.predict(X_record)[0]

probabilities = model.predict_proba(X_record)[0]

confidence = probabilities[prediction]


# ==================================================
# 5. DISPLAY RESULT
# ==================================================

print("\n===== SAVED MODEL PREDICTION =====")

print("Prediction:", prediction)
print(f"Confidence: {confidence:.2%}")
