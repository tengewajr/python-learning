#Objective 
#Create a Python program that takes motor sensor information and predicts whether the motor is likely to experience a failure. 
 
import pandas as pd

print("===== MOTOR FAULT DETECTION =====")

# STEP 1 — Load the dataset
df = pd.read_csv("week4/day1/ai4i2020.csv")

print("\nLoading the original dataset...")
print(df.head())

print("\nOriginal Dataset Shape:")
print(df.shape) 

# STEP 2 - Prepare the Data (Clean and prepare the dataset for analysis)
print("\n===== MISSING VALUES =====")
missing_values = df.isnull().sum()
print(missing_values)

df = df.dropna()  # Remove any rows with missing values
print("\nDataset Shape after removing missing values:")
print(df.shape)

# STEP 3 — Train the Model 
# (Split the dataset into training and testing sets, train a Decision Tree model using the better-performing model from day 4, and evaluate its performance)
# Select features and target

print("\n===== TRAINING THE MODEL =====")
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

# Encode the categorical Type feature
X = pd.get_dummies(X, columns=["Type"], dtype=int)

# Select target variable
y = df["Machine failure"]

# Split the dataset into training and testing sets
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
    X, 
    y, 
    test_size=0.2, 
    random_state=42,
    stratify=y # Ensure that the class distribution is preserved in both training and testing sets
)

print("\nTraining records:", len(X_train))
print("Testing records:", len(X_test))

# Since decision tree performed better in day 4, we will use it for this model
from sklearn.tree import DecisionTreeClassifier
model = DecisionTreeClassifier(random_state=42)

# Train the Decision Tree model
model.fit(X_train, y_train)
model_predictions = model.predict(X_test)

print("\nModel training completed successfully!")

# STEP 4 — Evaluate the Model
# Evaluate the model's performance using accuracy, precision, recall, and F1-score
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix
)

accuracy = accuracy_score(y_test, model_predictions)
precision = precision_score(
    y_test, 
    model_predictions,
    zero_division=0
)
recall = recall_score(
    y_test, 
    model_predictions,
    zero_division=0
)
f1 = f1_score(
    y_test, 
    model_predictions,
    zero_division=0
)

conf_matrix = confusion_matrix(y_test, model_predictions)

print("\n===== MODEL EVALUATION =====")
print(f"Accuracy: {accuracy:.2%}")
print(f"Precision: {precision:.2%}")
print(f"Recall: {recall:.2%}")
print(f"F1-Score: {f1:.2%}")

print("\nConfusion Matrix:")
print(conf_matrix)

# Interpretation of the confusion matrix
tn, fp, fn, tp = conf_matrix.ravel()

print(f"\nTrue Negatives: {tn}")
print(" Healthy motors correctly identified as healthy.")

print(f"False Positives: {fp}")
print(" Healthy motors incorrectly identified as faulty.")

print(f"False Negatives: {fn}")
print(" Faulty motors incorrectly identified as healthy.")

print(f"True Positives: {tp}")
print(" Faulty motors correctly identified as faulty.")

# STEP 5 - Predicting Motor Failure for New Data
# Create a new data point for predicting motor failure based on sensor readings
# A user should be able to input new sensor readings, and the program will predict whether the motor is likely to experience a failure.

print("\n===== PREDICTING MOTOR FAILURE FOR NEW DATA =====")
# Example new data point (user should be able to input these values)
print("Please enter the following motor sensor readings:")

new_data_Type = str(input("Enter the motor type (H, L, M): ")).strip().upper()

if new_data_Type not in ["H", "L", "M"]:
    print("Invalid motor type. Please enter H, L, or M.")
    exit()

new_data_AirTemp = float(input("Enter the air temperature [K]: "))
new_data_ProcessTemp = float(input("Enter the process temperature [K]: "))
new_data_RotationalSpeed = int(input("Enter the rotational speed [rpm]: "))
new_data_Torque = float(input("Enter the torque [Nm]: "))
new_data_ToolWear = int(input("Enter the tool wear [min]: "))

# Create a DataFrame for the new data point
new_data = pd.DataFrame({
    "Type": [new_data_Type],
    "Air temperature [K]": [new_data_AirTemp],
    "Process temperature [K]": [new_data_ProcessTemp],
    "Rotational speed [rpm]": [new_data_RotationalSpeed],
    "Torque [Nm]": [new_data_Torque],
    "Tool wear [min]": [new_data_ToolWear]
})

# Encode the categorical Type feature
new_data = pd.get_dummies(new_data, columns=["Type"], dtype=int)

# Make sure that the new data has exactly the same columns and column order as the training data (X_train)
new_data = new_data.reindex(columns=X_train.columns, fill_value=0)

# Make prediction for the new data point
new_prediction = model.predict(new_data)
print(f"\nPrediction for the new data point: {new_prediction[0]}")

if new_prediction[0] == 1:
    print("POSSIBLE MOTOR FAILURE")
else:
    print("MOTOR OPERATING NORMALLY")   
    