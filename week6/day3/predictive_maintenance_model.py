# Day 3 - Build the Predictive Maintenance Model

import pandas as pd

from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import(
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix
)

print("==============================================")
print("     PREDICTIVE MAINTENANCE MODEL")
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
    "Tool wear [min]",
]

X = df[features]

# ==================================================
# 3. SELECT TARGET
# ==================================================

y = df["Failure_Soon"]

print("\n===== FEATURES =====")
for feature in features:
    print("-", feature)

print("\nTarget: Failure_Soon")

# ==================================================
# 4. CHRONOLOGICAL TRAIN / TEST SPLIT
# ==================================================

split_index = int(len(df) * 0.80) # Finding the cut-off point

# Splitting the features (X)
X_train = X.iloc[:split_index] # slices the data from the very beginning up to (but not including) the 80% mark.
X_test = X.iloc[split_index:] # slices the data from the 80% mark all the way to the very end.

# Splitting the target/label (y)
y_train = y.iloc[:split_index]
y_test = y.iloc[split_index:]

print("\n===== DATA SPLITS =====")
print("Training Records:",len(X_train))
print("Testing Records:",len(X_test))

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
# 6. PREDICT
# ==================================================

predictions = model.predict(X_test)

# ==================================================
# 7. EVALUATE
# ==================================================

accuracy = accuracy_score(
    y_test,
    predictions
)

precision = precision_score(
    y_test,
    predictions,
    zero_division=0
)

recall = recall_score(
    y_test,
    predictions,
    zero_division=0
)

f1 = f1_score(
    y_test,
    predictions,
    zero_division=0
)

conf_matrix = confusion_matrix(
    y_test,
    predictions
)

print("\n===== MODEL EVALUATION =====")

print(f"Accuracy:  {accuracy:.2%}")
print(f"Precision: {precision:.2%}")
print(f"Recall:    {recall:.2%}")
print(f"F1-score:  {f1:.2%}")

print("\nConfusion Matrix:")
print(conf_matrix)

# ==================================================
# 8. CONFUSION MATRIX INTERPRETATION
# ==================================================

tn, fp, fn, tp = conf_matrix.ravel()

print("\n===== CONFUSION MATRIX =====")

print("True Negatives:", tn)
print("False Positives:", fp)
print("False Negatives:", fn)
print("True Positives:", tp)

# ==================================================
# 9. FEATURE IMPORTANCE
# ==================================================

print("\n===== FEATURE IMPORTANCE =====")

feature_importance = pd.Series(
    model.feature_importances_,
    index=features
).sort_values(ascending=False)

print((feature_importance).round(3))

print("\n===== TEST SET CLASS DISTRIBUTION =====")

print(
    "Failure_Soon = 0:",
    (y_test == 0).sum()
)

print(
    "Failure_Soon = 1:",
    (y_test == 1).sum()
)

print(
    f"Failure_Soon = 0: "
    f"{(y_test == 0).mean() * 100:.2f}%"
)

print(
    f"Failure_Soon = 1: "
    f"{(y_test == 1).mean() * 100:.2f}%"
)
