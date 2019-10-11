# --------------
# Project Title :- Banking Inferences
# Task 1 :- Confidence Interval
# Task Description :- Our first task will involve loading data and finding the confidence interval.

import pandas as pd
import scipy.stats as stats
import math
import numpy as np
import warnings

warnings.filterwarnings('ignore')
#Sample_Size
sample_size=2000

#Z_Critical Score
z_critical = stats.norm.ppf(q = 0.95)  
print("Z critical value " + str(z_critical))

# path        [File location variable]
data=pd.read_csv(path)

# creating a data sample
data_sample = data.sample(n=sample_size,random_state=0)

# Storing the mean of installment column of 'sample_data'
sample_mean = data_sample['installment'].mean()
print(" Sample Mean "+ str(sample_mean))

# Storing the standard devaition of installment column of 'sample_data'
sample_std = data_sample['installment'].std()
print("Sample Standard Deviation "+ str(sample_std))

# Finding the margin of error using 'z_critical'(given),'sample_std' and 'sample_size'
margin_of_error = (z_critical * sample_std)/math.sqrt(sample_size)
print("Margin of error "+ str(margin_of_error))

# Finding the confindence interval using 'sample_mean' and 'margin_of_error'
confidence_interval = sample_mean - margin_of_error , sample_mean + margin_of_error
print("Confidence Interval "+ str(confidence_interval))

# storing the mean of installment column of 'data' (population mean)
true_mean = data['installment'].mean()
print("True Mean " + str(true_mean))





# --------------
# Task 2:- CLT
# Task Description:- Let's now find out if Central Limit Theorem holds for installment column
import matplotlib.pyplot as plt
import numpy as np

#Different sample sizes to take
sample_size=np.array([20,50,100])

#Code starts here
fig, axes = plt.subplots(nrows=3,ncols=1,figsize=(15,10))

print(len(sample_size))
for i in range(len(sample_size)):
    m=[]
    for j in range(1000):
        data_sample = data['installment'].sample(n=sample_size[i])
        m.append(data_sample.mean())
    mean_series = pd.Series(m) 
    axes[i].hist(mean_series) 




       


# --------------
# Task 3:- Small Business Interests
# Task Description:- The bank manager believes that people with purpose as 'small_business' have been given int.rate more due to the risk assosciated

# Let's do a hypothesis testing(one-sided) on that belief

# Null Hypothesis H_0 : μ= 12 %
# Meaning: There is no difference in interest rate being given to people with purpose as 'small_business'

# Alternate Hypothesis H_1: μ>12 %
# Meaning: Interest rate being given to people with purpose as 'small_business' is higher than the average interest rate

#Importing header files
from statsmodels.stats.weightstats import ztest

# Code starts here
# From the column int.rate of 'data', removing the % character and converting the column into float.
data['int.rate'] = data['int.rate'].str.replace('%','')

# dividing the values of int.rate with 100
data['int.rate'] = data['int.rate'].astype(float).apply(lambda x:x/100)

# Applying ztest
z_statistic,p_value = ztest(x1=data[data['purpose']=='small_business']['int.rate'],value=data['int.rate'].mean(),alternative='larger')

# If 'p-value is less than 0.05, we can reject the null hypothesis, If 'p-value is greater than 0.05, we can't reject the null hypothesis,
print(z_statistic,p_value)

# Here we can reject the null hypothesis as p_value < 0.05











# --------------
# Task 4:- Installment vs Loan Defaulting
# Task Description :- The bank thinks that monthly installments (installment) customers have to pay might have some sort of effect on loan defaulters

# Let's do hypothesis testing(two-sided) on that

# Null Hypothesis H_0:  :μ¨D(yes)==¨Dμ(no)
# Meaning: There is no difference in installments being paid by loan defaulters and loan non defaulters

# Alternate Hypothesis H_1: :μ¨D(yes)¨D̸=μ(no)
# Meaning: There is difference in installments being paid by loan defaulters and loan non defaulters

#Importing header files
from statsmodels.stats.weightstats import ztest

#Code starts here
z_statistic,p_value = ztest(x1 = data[data['paid.back.loan']=='No']['installment'],
x2 = data[data['paid.back.loan']=='Yes']['installment']
)

print(z_statistic,p_value)

# Here p-value is less than 0.05 hence we can reject the null hypothesis and state that
# There is some sort of effect on installment being paid on loan defaulters.





# --------------
# Task 5:- Purpose vs Loan Defaulting
# Task Description:- Another thing bank suspects is that there is a strong association between purpose of the loan(purpose column) of a person and whether that person has paid back loan (paid.back.loan column)

# Since both are categorical columns, we will do chi-square test to test the same.
# ----------------------------------------------------------------------------
# Null Hypothesis : Distribution of purpose across all customers is same.
# -----------------------------------------------------------------------------
# Alternative Hypothesis : Distribution of purpose for loan defaulters and non
#  defaulters is different.
# ------------------------------------------------------------------------------

#Importing header files
from scipy.stats import chi2_contingency

#Critical value 
critical_value = stats.chi2.ppf(q = 0.95, # Find the critical value for 95% confidence*
                      df = 6)   # Df = number of variable categories(in purpose) - 1
print(critical_value)
#Code starts here

# value counts of purpose when loan is paid
yes = data[data['paid.back.loan'] == 'Yes']['purpose'].value_counts()
# print(yes)

# value counts of purpose when loan is not paid
no = data[data['paid.back.loan']=='No']['purpose'].value_counts()
# print(no)

# Creating the observed dataframe with value counts of yes or no
observed = pd.concat([yes.transpose(),no.transpose()],axis=1,keys=['Yes','No'])
# print(observed)

# Performing chi squared test on observed dataframe.
chi2,p,dof,ex = chi2_contingency(observed)
# print(chi2)

# Here chi squared statistic exceeds the critical value, hence we reject null hypothesis that the two distributions are the same and we can state that two distributions are different.





