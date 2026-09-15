# Day 4 - Program 1
# Analyze Model Predictions

import pandas as pd

from sklearn.ensemble import RandomForestClassifier


print("==============================================")
print("       ANALYZE MODEL PREDICTIONS")
print("==============================================")


# ==================================================
# 1. LOAD PROCESSED DATA
# ==================================================

df = pd.read_csv(
    "week6/day2/processed_motor_data.csv"
)

print("\n===== DATASET =====")
print("Records:", len(df))
print("Columns:", df.columns.tolist())

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
X_test = X.iloc[split_index:]

y_train = y.iloc[:split_index]
y_test = y.iloc[split_index:]


# ==================================================
# 5. TRAIN RANDOM FOREST
# ==================================================

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)


# ==================================================
# 6. MAKE PREDICTIONS
# ==================================================

predictions = model.predict(X_test)


# ==================================================
# 7. CREATE COMPARISON TABLE
# ==================================================

results = pd.DataFrame({
    "Actual": y_test.values,
    "Predicted": predictions
})

print("\n===== ACTUAL VS PREDICTED =====")
print(results.head(20))

# ==================================================
# 8. IDENTIFY EACH TYPE OF RESULT
# ==================================================

results["Result"] = "Unknown"

results.loc[
    (results["Actual"] == 0) &
    (results["Predicted"] == 0),
    "Result"
] = "True Negative"

results.loc[
    (results["Actual"] == 0) &
    (results["Predicted"] == 1),
    "Result"
] = "False Positive"

results.loc[
    (results["Actual"] == 1) &
    (results["Predicted"] == 1),
    "Result"
] = "True Positive"

results.loc[
    (results["Actual"] == 1) &
    (results["Predicted"] == 0),
    "Result"
] = "False Negative"


# ==================================================
# 9. COUNT EACH RESULT
# ==================================================

print("\n===== PREDICTION RESULTS =====")

print(
    results["Result"].value_counts()
)

# ==================================================
# 10. SHOW COUNTS CLEARLY
# ==================================================

print("\n===== COUNTS =====")

print(
    "True Negatives:",
    (results["Result"] == "True Negative").sum()
)

print(
    "False Positives:",
    (results["Result"] == "False Positive").sum()
)

print(
    "True Positives:",
    (results["Result"] == "True Positive").sum()
)

print(
    "False Negatives:",
    (results["Result"] == "False Negative").sum()
)
