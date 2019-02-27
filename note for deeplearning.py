# -*- coding: utf-8 -*-
# Data preproessing
# Importng the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importting the dataset
datasets=pd.read_csv('Data.csv')
X = datasets.iloc[:,:-1].values#all columns except the last one
y = datasets.iloc[:,3].values#iport the last column

# Taking care of missing data
from sklearn.preprocessing import Imputer#contains methods of preprocessing
imputer = Imputer(missing_values='NaN', strategy = 'mean', axis = 0, )
imputer = imputer.fit(X[:,1:3])
X[:,1:3] = imputer.transform(X[:,1:3] )

# Encoding categorical data
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_X = LabelEncoder()
X[:,0] = labelencoder_X.fit_transform(X[:,0])
#为了避免将文字替换成数字时候，数字产生排序的意义，进行以下操作：
# #制造三列，每一列代表一个国家，只有数字一存在 dummy bariables
# onehotencoder = OneHotEncoder(categorical_features = [0])
# X = onehotencoder.fit_transform(X).toarray()
# #最后一列可以用0/1表示
# labelencoder_y = LabelEncoder()
# y= labelencoder_y.fit_transform(y)

# # Splitting the dataset into the Training set and Test set
# from sklearn.cross_validation import train_test_split
# X_train, X_test, y_train, y_test = train_test_split(X , y,test_size = 0.2, random_state = 0)

# Feature scaling
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
