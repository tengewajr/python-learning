#Day 3 – Train the First Motor Fault Model 
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix
)


print("===== MOTOR FAULT DETECTION - DECISION TREE =====")


# STEP 1 — Load the dataset
df = pd.read_csv("week4/day1/ai4i2020.csv")


# STEP 2 — Select features and target
X = df[
    [
        "Type",
        "Air temperature [K]",
        "Process temperature [K]",
        "Rotational speed [rpm]",
        "Torque [Nm]",
        "Tool wear [min]"
    ]
]

y = df["Machine failure"]


# STEP 3 — Encode the categorical Type feature
X = pd.get_dummies(X, columns=["Type"], dtype=int)


print("\n===== PREPARED FEATURES =====")
print(X.head())


# STEP 4 — Split the dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)


print("\nTraining records:", len(X_train))
print("Testing records:", len(X_test))


# STEP 5 — Create the Decision Tree
model = DecisionTreeClassifier(random_state=42)


# STEP 6 — Train the model
model.fit(X_train, y_train)


print("\nModel training completed successfully!")


# STEP 7 — Make predictions
predictions = model.predict(X_test)


# STEP 8 — Evaluate the model
accuracy = accuracy_score(y_test, predictions)

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

conf_matrix = confusion_matrix(y_test, predictions)

print("\n===== MODEL EVALUATION =====")
print(f"Accuracy:  {accuracy:.2%}")
print(f"Precision: {precision:.2%}")
print(f"Recall:    {recall:.2%}")
print(f"F1-score:  {f1:.2%}")

print("\nConfusion Matrix:")
print(conf_matrix)   