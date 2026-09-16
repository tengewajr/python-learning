# Day 5 - Program 3
# Test the Saved Predictive Maintenance Model

import joblib
import pandas as pd


print("==============================================")
print("       TEST PREDICTIVE MAINTENANCE MODEL")
print("==============================================")


# ==================================================
# 1. LOAD SAVED MODEL
# ==================================================

model = joblib.load(
    "week6/day5/motor_model.pkl"
)

print("\nModel loaded successfully!")


# ==================================================
# 2. ENTER NEW MOTOR READINGS
# ==================================================

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
# 3. CREATE INPUT DATA
# ==================================================

new_motor = pd.DataFrame([{
    "Air temperature [K]": air_temperature,
    "Process temperature [K]": process_temperature,
    "Rotational speed [rpm]": rotational_speed,
    "Torque [Nm]": torque,
    "Tool wear [min]": tool_wear
}])


print("\n===== MOTOR INPUT =====")
print(new_motor.to_string(index=False))


# ==================================================
# 4. MAKE PREDICTION
# ==================================================

prediction = model.predict(new_motor)[0]


# ==================================================
# 5. GET CONFIDENCE
# ==================================================

probabilities = model.predict_proba(new_motor)[0]

confidence = probabilities[prediction]


# ==================================================
# 6. DISPLAY RESULT
# ==================================================

print("\n===== RESULT =====")

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
    