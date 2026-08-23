# Program 2 – Confusion Matrix and Classification Report

"""
Evaluate the Iris Decision Tree model using:

1. Accuracy
2. Confusion Matrix
3. Classification Report
"""

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report
)


print("==== IRIS MODEL EVALUATION ====")


# 1. Load the dataset
iris = load_iris()


# 2. Separate features and labels
X = iris.data
y = iris.target


# 3. Split the dataset into training and testing data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# 4. Create the Decision Tree model
model = DecisionTreeClassifier(random_state=42)


# 5. Train the model
model.fit(X_train, y_train)


# 6. Make predictions
predictions = model.predict(X_test)


# 7. Calculate accuracy
accuracy = accuracy_score(y_test, predictions)

print(f"\nModel Accuracy: {accuracy:.2%}")


# 8. Create confusion matrix
matrix = confusion_matrix(y_test, predictions)

print("\nConfusion Matrix:")
print(matrix)


# 9. Display classification report
print("\nClassification Report:")
print(
    classification_report(
        y_test,
        predictions,
        target_names=iris.target_names
    )
)