#Program 2 – Explore a Dataset 
"""Use the Iris dataset from scikit-learn. 

Learn how to: 
• Load the dataset.  
• Display the data.  
• Identify the features.  
• Identify the target.  
• Find the number of records. 

Install 
pip install scikit-learn 

Git Task 
Commit and push today's work. 

Commit: 
Day 1 - Introduction to Machine Learning
"""

from sklearn.datasets import load_iris

# Load the Iris dataset
iris = load_iris()

# Dislay the data
print("==== IRIS DATASET ====")
print(iris.data)

# Display the feature names
print("\n==== FEATURES ====")
print(iris.feature_names)

# Display the target
print("\n==== TARGET ====")
print(iris.target)

# Display the target names
print("\n==== TARGET NAMES ====")
print(iris.target_names)

# Number of records
print("\n==== NUMBER OF RECORDS ====")
print(len(iris.data))