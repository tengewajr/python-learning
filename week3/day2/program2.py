# Program 2 – Make Your Own Prediction

"""
Train a Decision Tree using the Iris dataset,
then give the model new measurements and ask it
to predict the flower type repeatedly.

"""

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

print("===== IRIS FLOWER PREDICTION =====")

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

# 6. Check model accuracy
test_predictions = model.predict(X_test)

accuracy=accuracy_score(y_test, test_predictions)

print(f"\nModel accuracy: {accuracy:.2%}")

# 7. Keep asking for new flower measurements
while True:
    print("\nEnter new flower measurements")
    print("Format: Sepal Length Sepal Width, Petal Length, Petal Width")
    print("Enter 'q' to quit.")

    user_input = input ("Measurements: ")

    # Check if user wants to quit
    if user_input.lower() == "q":
        print("Thank you for using the Iris Flower Predictor!")
        break

    try:
        values = list(map(float, user_input.split()))

        if len(values) != 4:
            print ("Please enter exactly 4 measurements.")
            continue

        # Converts inputs into numbers
        new_flower = [values]

        # 8. Make prediction
        prediction = model.predict(new_flower)

        # 9. Convert numerical prediction to flower name
        predicted_flower=iris.target_names[prediction[0]]

        # 10. Display measurements
        print("\nNew Flower Measurements:")
        print(f"Sepal Length: {new_flower[0][0]} cm")
        print(f"Sepal Width:  {new_flower[0][1]} cm")
        print(f"Petal Length: {new_flower[0][2]} cm")
        print(f"Petal Width:  {new_flower[0][3]} cm")

        print(f"Predicted flower: {predicted_flower}")

    except ValueError:
        print("Invalid input. Please enter numbers only.")