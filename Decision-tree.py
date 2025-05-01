from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
import pandas as pd
from sklearn import tree
import matplotlib.pyplot as plt

# Sample dataset
data = {
    'Age': ['<=30', '<=30', '31-40', '>40', '>40'],
    'Income': ['High', 'High', 'High', 'Medium', 'Low'],
    'Student': ['No', 'No', 'No', 'No', 'Yes'],
    'Credit_rating': ['Fair', 'Excellent', 'Fair', 'Fair', 'Fair'],
    'Buys_computer': ['No', 'No', 'Yes', 'Yes', 'Yes']
}

# Create DataFrame
df = pd.DataFrame(data)

# Encode categorical features
le = LabelEncoder()
for column in df.columns:
    df[column] = le.fit_transform(df[column])

# Features and target
X = df.drop('Buys_computer', axis=1)
y = df['Buys_computer']

# Train decision tree
clf = DecisionTreeClassifier(criterion='entropy')  # Use 'gini' or 'entropy'
clf.fit(X, y)

# Visualize the tree
plt.figure(figsize=(12, 8))
tree.plot_tree(clf, feature_names=X.columns, class_names=['No', 'Yes'], filled=True)
plt.show()

# Predict a sample
sample = [[0, 0, 0, 0]]  # Encoded example: Age <=30, Income High, Student No, Credit_rating Fair
prediction = clf.predict(sample)
print("Prediction:", 'Yes' if prediction[0] == 1 else 'No')
