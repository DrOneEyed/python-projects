# importing libs
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('sample_data.csv')
print(dataset)

dataset.head()

dataset.describe()

dataset = dataset.drop_duplicates()
print(dataset)

dataset.describe()

dataset.isnull()

dataset.isnull().sum()

dataset.dropna(how='any', subset=['Country', 'Purchased'], inplace=True)

# Splitting dataset into independent & dependent variable
X = dataset[['Country', 'Age', 'Salary']].values
y = dataset['Purchased'].values
print(X)

print(y)

# replacing the missing values in the age & salary column with the mean
# import the SimpleImputer class from the sklearn library
from sklearn.impute import SimpleImputer
print(X[:, 1:3])

imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
imputer.fit(X[:, 1:3])
X[:, 1:3] = imputer.transform(X[:, 1:3])
print(X[:, 1:3])

# Handling Categorical Data
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
ct = ColumnTransformer(transformers=[('enconder', OneHotEncoder(), [0])], remainder='passthrough')
X = np.array(ct.fit_transform(X))
print(X)

print(y)

from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
y = le.fit_transform(y)
print(y)

# Splitting Dataset into Training and Test Set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=2)