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

data_path = (
    Path(__file__).resolve().parent
    / "motor_health_training_data.csv"
)

model_path = (
    Path(__file__).resolve().parent
    / "motor_health_model.pkl"
)


df = pd.read_csv(data_path)


print("==============================================")
print("       MOTOR HEALTH MODEL TRAINING")
print("==============================================")

print(f"Dataset size: {len(df)}")


# ==================================================
# 2. SELECT FEATURES AND TARGET
# ==================================================

features = [
    "temperature",
    "vibration",
    "current",
    "sound",
    "rpm"
]

target = "health_status"


X = df[features]
y = df[target]


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
    n_estimators=100,
    random_state=42
)


model.fit(X_train, y_train)


# ==================================================
# 5. PREDICTION
# ==================================================

y_pred = model.predict(X_test)


# ==================================================
# 6. EVALUATION
# ==================================================

accuracy = accuracy_score(
    y_test,
    y_pred
)

precision = precision_score(
    y_test,
    y_pred,
    average="weighted"
)

recall = recall_score(
    y_test,
    y_pred,
    average="weighted"
)

f1 = f1_score(
    y_test,
    y_pred,
    average="weighted"
)

cm = confusion_matrix(
    y_test,
    y_pred
)


print("\n==============================================")
print("             MODEL RESULTS")
print("==============================================")

print(f"Accuracy  : {accuracy * 100:.2f}%")
print(f"Precision : {precision * 100:.2f}%")
print(f"Recall    : {recall * 100:.2f}%")
print(f"F1 Score  : {f1 * 100:.2f}%")


print("\nConfusion Matrix:")
print(cm)


print("\nClassification Report:")
print(
    classification_report(
        y_test,
        y_pred
    )
)


# ==================================================
# 7. FEATURE IMPORTANCE
# ==================================================

print("\nFeature Importance:")

for feature, importance in zip(
    features,
    model.feature_importances_
):

    print(
        f"{feature:<15}: "
        f"{importance:.3f}"
    )


# ==================================================
# 8. SAVE MODEL
# ==================================================

joblib.dump(
    model,
    model_path
)


print("\n==============================================")
print("Model saved successfully.")
print(f"Saved to: {model_path}")
print("==============================================")