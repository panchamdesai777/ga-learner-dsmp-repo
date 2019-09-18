# Project Name: Loan Approval Analysis

# Task1: Load the data
# Task Description : Let's check which variable is categorical and which one is numerical so that you will get a basic idea about the features of the bank dataset.
# Import packages
import numpy as np
import pandas as pd
from scipy.stats import mode 
 
# code starts here
bank = pd.read_csv(path)
categorical_var = bank.select_dtypes(include='object')
print(categorical_var)
numerical_var = bank.select_dtypes(include='number')
print(numerical_var)
# code ends here

# Task 2:something is Missing!
# Task Description: Sometimes customers forget to fill in all the details or they don't want to share other details.
#                   Because of that, some of the fields in the dataset will have missing values. Now you have to check which columns 
#                   have missing values and also check the count of missing values each column has. If you get the columns that have
#                   missing values, try to fill them
# code starts here

banks = bank.drop(['Loan_ID'],axis=1)

# code to check the null values in dataframe in each column.
# print(banks.isnull().sum())

# code to calculate mode for banks dataframe. mode means most repeated values in dataframe
bank_mode = banks.mode().iloc[0]
print(type(bank_mode))

# code to fill all the missing values(NaN) with bank_mode.
banks = banks.fillna(bank_mode)

# code to check if all missing values(NaN) are filled.
print(banks.isnull().sum())

#code ends here


# Task 3: Loan Amount vs Gender
# Task Description: Now let's check the loan amount of an average person based on 'Gender', 'Married', 'Self_Employed'.
#                   This will give a basic idea of the average loan amount of a person.
# Code starts here

# print(banks)
avg_loan_amount = banks.pivot_table(index=['Gender','Married','Self_Employed'],values='LoanAmount')
print(avg_loan_amount)
# code ends here


# Task 4:  Loan Approval vs Employment
# Task Description: Now let's check the percentage of loan approved based on a person's employment type.
# code starts here

condition_1 = banks['Self_Employed']=='Yes'
condition_2 = banks['Loan_Status']=='Y'
condition_3 = banks['Self_Employed']=='No'

result1 = condition_1 & condition_2
result2 = condition_3 & condition_2

#store the count of results where Self_Employed == Yes and Loan_Status == Y.
loan_approved_se = len(banks[result1])

#store the count of results where Self_Employed == No and Loan_Status == Y.
loan_approved_nse = len(banks[result2])

Loan_Status = 614  # already given

percentage_se = (loan_approved_se / Loan_Status)*100 
percentage_nse = (loan_approved_nse/Loan_Status)*100

print(percentage_se)
print(percentage_nse)
# code ends here


# Task 5: Transform the loan tenure from months to years
# Task Description: A government audit is happening real soon! So the company wants to find out those applicants with long loan amount term.
# code starts here

#converting loan amount term from no of months to no of years
loan_term = banks['Loan_Amount_Term'].apply(lambda x:int(x) / 12)

print(loan_term)
# no of applicants having loan amount term >= 25 years
big_loan_term = len(bank[loan_term >= 25])

print(big_loan_term)
# code ends here


# Task 6: Income/ Credit History vs Loan Amount
# Task Description: Now let's check the average income of an applicant and the average loan given to a person based on their income.
# code starts here

# grouping the dataframe by Loan_Status 
loan_groupby = banks.groupby('Loan_Status')

# sub setting the groupby object to include only below two columns
loan_groupby = loan_groupby[['ApplicantIncome','Credit_History']]

# calculating the mean values of DataFrameGroupBy object "loan_groupby"
mean_values = loan_groupby.mean()

print(mean_values)
# code ends here


