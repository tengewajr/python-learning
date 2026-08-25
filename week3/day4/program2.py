#Program 2 – Compare Models 
"""
Try another model: 
Decision Tree Regressor 

Compare the two models. 

Questions: 
- Which model performed better? 
- Why do you think it performed better?
"""

from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import r2_score

print ("==== DECISION TREE REGRESSION MODEL 2 ====")
print ("\nCALIFORNIA HOUSING DATASET")
print ("USING DECISION TREE REGRESSOR")

# No. 1: Load the dataset
california_data = fetch_california_housing(as_frame=True)

# No. 2: Separate the features (X) and target variable (y)
X = california_data.data
y = california_data.target

# No. 3: Split into training and testing data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size = 0.2,
    random_state = 42,
)

# No. 4: Creating Decision Tree Regression Model
model = DecisionTreeRegressor(random_state=42)

# No. 5: Training the model
model.fit(X_train, y_train)

# No. 6: Making predictions
predictions = model.predict(X_test)

# No. 7: Evaluating the predictions
r2 = r2_score(y_test, predictions)

print("\nMODEL RESULTS")
print("-"*30)
print (f"R² score is: {r2:.2f}")

print("\nFirst 5 Predictions")
for value in predictions[:5]:
    print(f"Value: {value:.2f}")

