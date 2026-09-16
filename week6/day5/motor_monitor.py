# Day 5 - Program 4
# Motor Predictive Maintenance System - Version 1

import joblib
import pandas as pd


print("==============================================")
print("      MOTOR PREDICTIVE MAINTENANCE SYSTEM")
print("==============================================")


# ==================================================
# 1. LOAD TRAINED MODEL
# ==================================================

model = joblib.load(
    "week6/day5/motor_model.pkl"
)

print("\nTrained model loaded successfully!")


# ==================================================
# 2. COLLECT MOTOR READINGS
# ==================================================

print("\n===== ENTER MOTOR READINGS =====")

air_temperature = float(
    input("Air temperature [K]: ")
)

process_temperature = float(
    input("Process temperature [K]: ")
)

rotational_speed = float(
    input("Rotational speed [rpm]: ")
)

torque = float(
    input("Torque [Nm]: ")
)

tool_wear = float(
    input("Tool wear [min]: ")
)


# ==================================================
# 3. PREPARE INPUT FOR MODEL
# ==================================================

motor_data = pd.DataFrame([{
    "Air temperature [K]": air_temperature,
    "Process temperature [K]": process_temperature,
    "Rotational speed [rpm]": rotational_speed,
    "Torque [Nm]": torque,
    "Tool wear [min]": tool_wear
}])


# ==================================================
# 4. MAKE PREDICTION
# ==================================================

prediction = model.predict(motor_data)[0]

probabilities = model.predict_proba(
    motor_data
)[0]

confidence = probabilities[prediction]


# ==================================================
# 5. DISPLAY RESULT
# ==================================================

print("\n==============================================")
print("                  RESULT")
print("==============================================")


if prediction == 1:

    print("Prediction: FAILURE LIKELY")
    print(f"Confidence: {confidence:.2%}")

    print("\nRecommendation:")
    print(
        "Investigate the motor and inspect "
        "its operating conditions."
    )

else:

    print("Prediction: NORMAL")
    print(f"Confidence: {confidence:.2%}")

    print("\nRecommendation:")
    print(
        "No immediate warning from the model."
    )
    print("Continue monitoring.")


print("\n==============================================")
print("              MONITORING COMPLETE")
print("==============================================")
