# Day 4 - Program 2
# Investigate False Negatives

import pandas as pd

from sklearn.ensemble import RandomForestClassifier


print("==============================================")
print("       INVESTIGATE FALSE NEGATIVES")
print("==============================================")

# ==================================================
# 1. LOAD DATA
# ==================================================

df = pd.read_csv(
    "week6/day2/processed_motor_data.csv"
)


# ==================================================
# 2. FEATURES AND TARGET
# ==================================================

features = [
    "Air temperature [K]",
    "Process temperature [K]",
    "Rotational speed [rpm]",
    "Torque [Nm]",
    "Tool wear [min]"
]

X = df[features]
y = df["Failure_Soon"]


# ==================================================
# 3. CHRONOLOGICAL SPLIT
# ==================================================

split_index = int(len(df) * 0.80)

X_train = X.iloc[:split_index]
X_test = X.iloc[split_index:]

y_train = y.iloc[:split_index]
y_test = y.iloc[split_index:]


# ==================================================
# 4. TRAIN MODEL
# ==================================================

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)


# ==================================================
# 5. PREDICT
# ==================================================

predictions = model.predict(X_test)


# ==================================================
# 6. BUILD TEST RESULTS
# ==================================================

test_results = df.iloc[split_index:].copy()

test_results["Predicted"] = predictions


# ==================================================
# 7. FIND FALSE NEGATIVES
# ==================================================

false_negatives = test_results[
    (test_results["Failure_Soon"] == 1) &
    (test_results["Predicted"] == 0)
]


print("\n===== FALSE NEGATIVES =====")
print("Number of false negatives:", len(false_negatives))


# ==================================================
# 8. SHOW SENSOR VALUES
# ==================================================

columns_to_show = [
    "UDI",
    "Air temperature [K]",
    "Process temperature [K]",
    "Rotational speed [rpm]",
    "Torque [Nm]",
    "Tool wear [min]",
    "Failure_Soon",
    "Predicted"
]

print("\n===== SAMPLE FALSE NEGATIVES =====")

print(
    false_negatives[columns_to_show].head(10).to_string(index=False)
)