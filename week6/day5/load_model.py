# Day 5 - Program 2
# Load the Saved Predictive Maintenance Model

import joblib


print("==============================================")
print("       LOAD PREDICTIVE MAINTENANCE MODEL")
print("==============================================")


# ==================================================
# 1. LOAD SAVED MODEL
# ==================================================

model = joblib.load(
    "week6/day5/motor_model.pkl"
)


print("\nModel loaded successfully!")
print("Model type:", type(model).__name__)


# ==================================================
# 2. CHECK MODEL
# ==================================================

print("\n===== MODEL INFORMATION =====")

print("Number of trees:", model.n_estimators)
print("Random state:", model.random_state)


print("\nThe saved model is ready for prediction.")

