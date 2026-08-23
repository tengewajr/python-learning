# Program 3 – Test Size Experiment

"""
Investigate how changing the test size
affects model accuracy.

Test:
20%
30%
40%
"""

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score


print("==== TEST SIZE EXPERIMENT ====")


# Load the dataset
iris = load_iris()

X = iris.data
y = iris.target


# Test different test sizes
test_sizes = [0.2, 0.3, 0.4]


for test_size in test_sizes:

    # Split the dataset
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=test_size,
        random_state=42
    )


    # Create the model
    model = DecisionTreeClassifier(random_state=42)


    # Train the model
    model.fit(X_train, y_train)


    # Make predictions
    predictions = model.predict(X_test)


    # Calculate accuracy
    accuracy = accuracy_score(y_test, predictions)


    print(
        f"Test Size: {test_size:.0%} "
        f"| Accuracy: {accuracy:.2%}"
    )