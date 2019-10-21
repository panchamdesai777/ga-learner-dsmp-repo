### Project Overview

 # **Problem Statement**

This project is based on linear regression model.

You are a die hard Lego enthusiast wishing to collect as many board sets as you can. But before that you wish to be able to predict the price of a new lego product before its price is revealed so that you can budget it from your revenue. Since (luckily!), you are a data scientist in the making, you wished to solve this problem yourself. This dataset contains information on lego sets scraped from lego.com. Each observation is a different lego set with various features like how many pieces in the set, rating for the set, number of reviews per set etc. Your aim is to build a linear regression model to predict the price of a set.

## **About the dataset :**
The dataset has details of 12261 lego sets with the following 10 features :

age - Which age categories it belongs to
list_price - price of set in dollars
num_reviews - number of reviews per set
piece_count - number of pieces in that lego set
playstarrating - ratings
review_difficulty - difficulty level of the set
star_rating - ratings
theme_name - which theme it belongs
valstarrating - ratings
country - country name


### Learnings from the project

 After completing this project, I now have the better understanding of how to build a linear regression model. In this project, I have applied the following concepts.

- Train-test split
- Correlation between the features
- Linear Regression
- MSE and R2 Evaluation Metrics


### Approach taken to solve the problem

 - Data loading and splitting : Loading the dataset and splitting the data into train and test.
- Scatter plot : check the scatter_plot for different features vs target variable list_price. This tells us which features are highly correlated with the target variable list_price and help us predict it better.
- Remove highly correlated columns : Features highly correlated with each other adversely affect our lego pricing model. Thus we keep a inter-feature correlation threshold of 0.75. If two features are correlated and with a value greater than 0.75, remove one of them.
- Make prediction : Intialize the model and make prediction . To check the predictions are accurate calculate r2 error make sure r2 error should be greater than 0.5.
- Calculate Residues : To check how much difference is present between train values and predicted values .


