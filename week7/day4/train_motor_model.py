
# Week 7 Day 4
# Train Motor Health Classification Model

import pandas as pd
import joblib

from pathlib import Path

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report
)


# ==================================================
# 1. LOAD DATA
# ==================================================

BASE_DIR = Path(__file__).resolve().parent

data_path = BASE_DIR / "motor_health_training_data.csv"
model_path = BASE_DIR / "motor_health_model.pkl"

df = pd.read_csv(data_path)

print("==============================================")
print("        MOTOR HEALTH MODEL TRAINING")
print("==============================================")

print(f"Dataset size: {len(df)}")


# ==================================================
# 2. SELECT FEATURES AND TARGET
# ==================================================

FEATURES = [
    "temperature",
    "vibration",
    "current",
    "sound",
    "rpm"
]

TARGET = "health_status"

X = df[FEATURES]
y = df[TARGET]


# ==================================================
# 3. TRAIN / TEST SPLIT
# ==================================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

print(f"Training records: {len(X_train)}")
print(f"Testing records : {len(X_test)}")


# ==================================================
# 4. TRAIN RANDOM FOREST
# ==================================================

model = RandomForestClassifier(
    n_estimators=200,
    random_state=42,
    class_weight="balanced",
    min_samples_leaf=2,
    max_features="sqrt"
)

model.fit(X_train, y_train)


# ==================================================
# 5. MODEL PREDICTIONS
# ==================================================

y_pred = model.predict(X_test)


# ==================================================
# 6. MODEL EVALUATION
# ==================================================

accuracy = accuracy_score(y_test, y_pred)

precision = precision_score(
    y_test,
    y_pred,
    average="macro",
    zero_division=0
)

recall = recall_score(
    y_test,
    y_pred,
    average="macro",
    zero_division=0
)

f1 = f1_score(
    y_test,
    y_pred,
    average="macro",
    zero_division=0
)

class_order = [
    "HEALTHY",
    "WARNING",
    "FAULT"
]

cm = confusion_matrix(
    y_test,
    y_pred,
    labels=class_order
)


print("\n==============================================")
print("             MODEL RESULTS")
print("==============================================")

print(f"Accuracy       : {accuracy * 100:.2f}%")
print(f"Macro Precision: {precision * 100:.2f}%")
print(f"Macro Recall   : {recall * 100:.2f}%")
print(f"Macro F1 Score : {f1 * 100:.2f}%")


print("\nConfusion Matrix:")
print(cm)


print("\nClassification Report:")

print(
    classification_report(
        y_test,
        y_pred,
        labels=class_order,
        zero_division=0
    )
)


# ==================================================
# 7. FEATURE IMPORTANCE
# ==================================================

print("\nFeature Importance:")

for feature, importance in zip(
    FEATURES,
    model.feature_importances_
):

    print(f"{feature:<15}: {importance:.3f}")


# ==================================================
# 8. SAVE MODEL
# ==================================================

joblib.dump(
    model,
    model_path
)

print("\n==============================================")
print("Model saved successfully.")
print(f"Location: {model_path}")
print("==============================================")
