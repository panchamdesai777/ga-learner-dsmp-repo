# --------------
# Task 1:- Data Loading and Splitting
# Task Description:- The first step is to load the dataset and see what it looks like. Additionally, split it into train and test set.

import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split

# path- variable storing file path
df = pd.read_csv(path)

X = df.drop('Price',axis = 1)
print(X.head(1))

y = df['Price']
print(y.head(1))

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3,random_state =6)

corr = X_train.corr()
#Code starts here


# --------------
# Task 2:- Prediction Using Linear Regression
# Task Description:- Now let's come to the actual task,i.e, predicting the price of the house using linear regression. We will check the model performance using r^2 score
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# Code starts here
regressor = LinearRegression()

regressor.fit(X_train,y_train)

y_pred = regressor.predict(X_test)

r2 = round(r2_score(y_test,y_pred),2)

print(r2)


# --------------
# Task 3:- Prediction Using Lasso
# Task Description:- In this task, let's predict the price of the house using a lasso regressor. Check if there is any improvement in the prediction.
from sklearn.linear_model import Lasso
# Code starts here

lasso = Lasso()

lasso.fit(X_train,y_train)

lasso_pred = lasso.predict(X_test)

r2_lasso = round(r2_score(y_test,lasso_pred),2)

print(r2_lasso)


# --------------
# Task 4:- Prediction Using Ridge
# Task Description:- There wasn't a clear improvement after applying the lasso regressor; that once again drives home the point that it's not necessary that the model will improve after regularization.Now, let's check the house price prediction using a ridge regressor.

from sklearn.linear_model import Ridge

# Code starts here

ridge = Ridge()

ridge.fit(X_train,y_train)

ridge_pred = ridge.predict(X_test)

r2_ridge = round(r2_score(y_test,y_pred),2)

print(r2_ridge)
# Code ends here


# --------------
# Task 5:- Prediction Using Cross Validation
# Task Description:- Now let's predict the house price using cross-validated estimators which is the part of the Model selection: choosing estimators and their parameters.

from sklearn.model_selection import cross_val_score

#Code starts here

regressor = LinearRegression()

score = cross_val_score(regressor,X_train,y_train,cv=10)

mean_score = np.mean(score)

print(mean_score)


# --------------
# Task 6:- Prediction Using Polynomial Regressor
# Task Description:- As you can see that there is very less improvement(~1%), even after applying the regularization and cross-validation score. Now let's perform the prediction using a polynomial regressor to generate second-degree polynomial features.

from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline

#Code starts here

model = make_pipeline(PolynomialFeatures(2),LinearRegression())

model.fit(X_train,y_train)

y_pred = model.predict(X_test)

r2_poly = round(r2_score(y_test,y_pred),2)

print(r2_poly)



