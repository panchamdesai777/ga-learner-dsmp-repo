# --------------
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


# --------------
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


# --------------
# Code starts here

# print(banks)

avg_loan_amount = banks.pivot_table(index=['Gender','Married','Self_Employed'],values='LoanAmount')

print(avg_loan_amount)
# code ends here



# --------------
# code starts here



condition_1 = banks['Self_Employed']=='Yes'
condition_2 = banks['Loan_Status']=='Y'
condition_3 = banks['Self_Employed']=='No'

result1 = condition_1 & condition_2
result2 = condition_3 & condition_2

loan_approved_se = len(banks[result1])

loan_approved_nse = len(banks[result2])

Loan_Status = 614
print(loan_approved_se)
print(loan_approved_nse)

percentage_se = (loan_approved_se / Loan_Status)*100 
percentage_nse = (loan_approved_nse/Loan_Status)*100

print(percentage_se)
print(percentage_nse)
# code ends here


# --------------
# code starts here

#converting loan amount term from no of months to no of years
loan_term = banks['Loan_Amount_Term'].apply(lambda x:int(x) / 12)

print(loan_term)

# no of applicants having loan amount term >= 25 years

big_loan_term = len(bank[loan_term >= 25])
print(big_loan_term)
# code ends here


# --------------
# code starts here

# grouping the dataframe by Loan_Status 
loan_groupby = banks.groupby('Loan_Status')

# sub setting the groupby object to include only below two columns
loan_groupby = loan_groupby[['ApplicantIncome','Credit_History']]

# calculating the mean values of DataFrameGroupBy object "loan_groupby"
mean_values = loan_groupby.mean()

print(mean_values)
# code ends here


