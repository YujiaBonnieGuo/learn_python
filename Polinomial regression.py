# Polinomial regression

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Position_Salaries.csv')
X = dataset.iloc[:, 1:2].values#make sure x is a matrix
y = dataset.iloc[:, 2].values

# Splitting the dataset into the Training set and Test set
'''from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)'''

# Feature Scaling
"""from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
sc_y = StandardScaler()
y_train = sc_y.fit_transform(y_train)"""

# Fitting Linear Regression to the dataset
from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
lin_reg.fit(X,y)

# Fitting Polynomial Regression to the dataset
from sklearn.preprocessing import PolynomialFeatures
poly_reg = PolynomialFeatures(degree = 4)   # 选择方程是几阶的，阶数越多越拟合与曲线
X_poly = poly_reg.fit_transform(X)          # 创建多项式每一项对应的值
poly_reg.fit(X_poly, y)                     # 将其规模适应于输出值y
lin_reg_2 = LinearRegression()              # 调用线性回归方程
lin_reg_2.fit(X_poly, y)                    # 创建多项式线性方程

 # Visualising the Linear Regressino results
 plt.scatter(X, y, color = 'red')
 plt.plot(X, lin_reg.predict(X), color = 'blue')
 plt.title('Truth of Bluff (Linear Regression)')
 plt.xlabel('Position level')
 plt.ylabel('Salary')
 plt.show()

 # Visualising the Polynomial Regressino results

 #在X的范围内将X的取值增多，使得曲线更加光滑
 X_grid = np.arange(min(X),max(X),0.1)
 X_grid = X_grid.reshape((len(X_grid),1))

 plt.scatter(X, y, color = 'red')
 plt.plot(X_grid, lin_reg_2.predict(poly_reg.fit_transform(X_grid)), color = 'green')
 plt.title('Truth of Bluff (Polynomial Regression)')
 plt.xlabel('Position level')
 plt.ylabel('Salary')
 plt.show()

# Predicting a new result with Linear Regression
lin_reg.predict(6.5)

# Predicting a new result with Polynomial Regression
lin_reg_2.predict(poly_reg.fit_transform(6.5))

