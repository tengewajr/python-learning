# Day 4 - Program 4
# Feature Importance

import pandas as pd

from sklearn.ensemble import RandomForestClassifier


print("==============================================")
print("          FEATURE IMPORTANCE")
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
y_train = y.iloc[:split_index]


# ==================================================
# 4. TRAIN MODEL
# ==================================================

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)


# ==================================================
# 5. FEATURE IMPORTANCE
# ==================================================

importance = pd.Series(
    model.feature_importances_,
    index=features
).sort_values(ascending=False)


print("\n===== FEATURE IMPORTANCE =====")

print(
    importance.round(3)
)