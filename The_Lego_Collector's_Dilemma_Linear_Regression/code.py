# --------------
                        # Project Title :- The Lego Collector's Dilemma

# Task 1:- Data loading and splitting
# Task Description:- load the dataset and see how it looks like. Additionally, split it into train and test set.

import pandas as pd
import numpy as np
from sklearn.cross_validation import train_test_split
# code starts here

df = pd.read_csv(path)

print(df.head(5))

# splitting the features (independent variables)
X = df[['ages','num_reviews','piece_count','play_star_rating','review_difficulty','star_rating','theme_name','val_star_rating','country']]

# splitting the Target (dependent variable)
y = df['list_price']

# splitting dataframe into 70% train data and 30% test data
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3,random_state = 6)

# code ends here



# --------------
# Task 2:- Predictor Check!
# task Description:- Let's check the scatter_plot for different features vs target variable list_price. This tells us which features are highly correlated with the target variable list_price and help us predict it better.

import matplotlib.pyplot as plt

# code starts here        

cols = X_train.columns
print(cols)

fig, axes = plt.subplots(nrows = 3,ncols =3,figsize=(15,15))
for i in range(0,3):
     for j in range(0,3):
        col = cols[i*3 + j]
        axes[i,j].scatter(X_train[col],y_train)
        axes[i,j].xlabel = X_train[col]
        axes[i,j].ylabel = y_train
        


# code ends here



# --------------
# Task 3:Reduce feature redundancies!
# Task Description: Features highly correlated with each other adversely affect our lego pricing model. Thus we keep a inter-feature correlation threshold of 0.75. If two features are correlated and with a value greater than 0.75, remove one of them.

# Code starts here
import seaborn as sns

corr = X_train.corr()

sns.heatmap(corr,annot=True)

# features of play_star_rating, val_star_rating and star_ratin have a correlation of greater than 0.75.
# hence dropping these two columns to improve model efficiency.
X_train.drop(columns=['play_star_rating','val_star_rating'],inplace=True)

X_test.drop(columns=['play_star_rating','val_star_rating'],inplace=True)
# Code ends here


# --------------
# Task 4:- Is my price prediction ok?
# Task Description:- Now let's come to the actual task, using linear regression to predict the price. We will check the model accuracy using r^2 score and mse (If model is bad, please keep extra money for the sets!).

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Code starts here

regressor = LinearRegression()

regressor.fit(X_train,y_train)

y_pred = regressor.predict(X_test)

mse = mean_squared_error(y_test,y_pred)
print(mse)

r2 =  r2_score ( y_test , y_pred)
print(r2)
# Code ends here


# --------------
# Task 5:- Residual check!
# Task Description:- Based on the distance between the true target y_test and predicted target y_pred, also known as the residual the cost function is defined. Let's look at the residual and visualize the errors in the model.


# Code starts here

data = pd.DataFrame({'actual':y_test,'predicted':y_pred})

print(data)

residual = y_test - y_pred

print(residual)

residual.hist()

# Code ends here


