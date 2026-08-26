# Day 5 – Mini Machine Learning Project 
"""Build a small ML project that predicts whether a student will Pass or Fail. 
Using a small CSV dataset that I made "student_data.csv"
"""

import pandas as pd

# STEP 1 - Load the dataset using Pandas
print("==== STUDENT PERFORMANCE PREDICTION DATASET ====")

df = pd.read_csv("week3/day5/student_data.csv")
print("\nOriginal Dataset")
print(df)

# STEP 2 - Explore the dataset
print("==== EXPLORING THE DATASET ====")
# Displaying number of records
print("\nNumber of Records:")
print(len(df))

# Display Columns
print("\nColumns:")
print(df.columns.to_list())

# Display first few records
print("\nFirst 5 records:")
print(df.head())

# Display 5 last records
print("\nLast 5 records:")
print(df.tail(5))

# Display 5 randomly selected records
print("\nRandomly 5 selected records:")
print(df.sample(5))

# Display Missing Values
print("\nMissing Values:")
print(df.isnull().sum())

# STEP 3 - Identifying Features and Targets
print("==== IDENTIFYING FEATURES (X) AND TARGET (y)")

X = df.drop(columns=["Result"]) # Features
# Alternatively way..... X = df[["StudyHours", "Attendance", "Assignments"]]
y = df["Result"] # Targets

# Displaying the First 5 features
print("\nFeatures (X):")
print(X.head()) 

# Displaying the First 5 targets
print("\nTarget (y):")
print(y.head())

# STEP 4 - Training a Model using a Decision Tree Classifier
print("==== TRAINING A MODEL ====")

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

# Spliting the dataset into Training data and testing data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("\nTraining records: ",len(X_train))
print("Testing records: ",len(X_test))

# Creating the model
model = DecisionTreeClassifier(random_state=42)

# Training the Model
model.fit(X_train,y_train)

print("\nModel training completed successfully!")

# STEP 5 - Making Predictions
print("\n==== NEW STUDENT PREDICTION ====")

study_hours = float(input("Enter study hours: "))
attendance = float(input("Enter the attendance (%): "))
assignments = float(input("Enter the assignment (%): "))

# Create a Dataframe so the feature names match the training data
new_student = pd.DataFrame ([{
    "StudyHours": study_hours,
    "Attendance": attendance,
    "Assignments": assignments
}])

# Make prediction
predictions = model.predict(new_student)

print("\nNew student:")
print(new_student)

print(f"Predicted result: {predictions[0]}")

# STEP 6 - Evaluating the Model
print("==== EVALUATING THE MODEL ====")

# Make predictions for the test dataset
test_predictions = model.predict(X_test)

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix
)

# Calculating accuracy
accuracy = accuracy_score(y_test, test_predictions)

# Calculating precision
precision = precision_score(
    y_test,
    test_predictions,
    pos_label="Pass"
)

# Calculating Recall
recall = recall_score(
    y_test, 
    test_predictions,
    pos_label="Pass"
)

# Calculating f-1 score
f1 = f1_score(
    y_test, 
    test_predictions,
    pos_label="Pass"
)

# Calculating confusion matrix
conf_matrix = confusion_matrix(
    y_test, 
    test_predictions,
    labels=["Fail","Pass"]
)

print("\nMODEL EVALUATION")
print("-"*30)

print(f"Accuracy: {accuracy:.2%}")
print(f"Precision: {precision:.2%}")
print(f"Recall: {recall:.2%}")
print(f"F1-score: {f1:.2%}")

print("\nConfusion Matrix: ")
print(conf_matrix)