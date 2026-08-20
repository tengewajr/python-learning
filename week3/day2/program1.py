# Program 1 – Train a Classification Model 
"""Use: Iris Dataset with Decision Tree 
Train a model to predict the type of Iris flower. 

You should: 
1. Load the dataset.  
2. Separate features and labels.  
3. Split the dataset into training and testing data.  
4. Create a Decision Tree model.  
5. Train it.  
6. Make predictions.  
7. Check the accuracy.  
"""

from sklearn.datasets import load_iris 
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

print ("==== IRIS CLASSIFICATION MODEL ====")

# 1. Load the datset
iris=load_iris()

# 2. Separate features and labels
X = iris.data
y = iris.target

# 3. Splits the dataset into training and testing data
X_train,X_test, y_train, y_test = train_test_split(
    X, 
    y, 
    test_size=0.2,
    random_state=42
) 

# 4. Create a Decision Tree Model
model = DecisionTreeClassifier(random_state=42)

# 5. Train the model
model.fit(X_train,y_train)

# 6. Make predictions
predictions=model.predict(X_test)

# 7. Check accuracy
accuracy=accuracy_score(y_test, predictions)

print(f"Accuracy: {accuracy:.2f}")


