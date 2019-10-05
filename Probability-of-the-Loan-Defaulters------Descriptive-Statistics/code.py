# --------------
                # Project Name :- Probability of the Loan Defaulters

# Task 1 :- Independence check !
# Task Description :- 
# To calculate the joint probability it's very important that conditions are idependent from each other. Les's check whether the condition fico credit score is greater than 700 and purpose == 'debt_consolidation' are independent from each other.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# code starts here
df = pd.read_csv(path)

# Probability p(A)for the event that fico credit score is greater than 700. 
p_a = df[df['fico'].astype(float)>700].shape[0]/df.shape[0]
print(p_a)

# probabilityp(B) for the event that purpose == 'debt_consolation'
p_b = df[df['purpose']=='debt_consolidation'].shape[0]/df.shape[0]
print(p_b)

df1 = df[df['purpose'] == 'debt_consolidation']

# probablity (B|A) for the event purpose == 'debt_consolidation' given 'fico' credit score is greater than 700
p_a_b = (p_a * p_b) / p_a
print(p_a_b)

# probablity (A|B) for the event 'fico' credit score is greater than 700 given that purpose == 'debt_consolidation' 
# p_b_a = (p_a_b * p_a)/p_b

p_b_a = df1[df1['fico'].astype(float)>700].shape[0]/df1.shape[0]
print(p_b_a)

# formula to check the independency P(A|B) == P(A)
if p_b_a == p_a:
    result=True
else:
    result=False

# Printing the final result
print(result)    
 
# code ends here


# --------------
# Task 2:- Bayes theorem
# Task Description:- Calculating conditional probabilty is the very important step. Let's calculate the bayes theorem for the probability of credit policy is yes and the person is given the loan.

# code starts here

#  probability p(A) for the event that paid.back.loan == Yes
prob_lp = df[df['paid.back.loan']=='Yes'].shape[0]/df.shape[0]
print(prob_lp)

# probability p(B) for the event that credit.policy == Yes
prob_cs = df[df['credit.policy']=='Yes'].shape[0]/df.shape[0]
print(prob_cs)

# given condition - ['paid.back.loan'] == 'Yes' and store it in variable new_df
new_df = df[df['paid.back.loan']=='Yes']

# probablityp(B|A) for the event credit.policy == 'Yes' given paid.back.loan == 'Yes' and store it in variable prob_pd_cs
prob_pd_cs = new_df[new_df['credit.policy']=='Yes'].shape[0]/new_df.shape[0]

# Calculating the conditional probability where the formala is given below:
# P(A∣B)= P(B∣A).P(A) / p(B)
# Storing the result of the event P(A|B) it in variable bayes
bayes = prob_pd_cs * prob_lp /prob_cs
print(bayes)

# code ends here


# --------------
# Task 3:- Purpose vs paid back loan
# Task Description:- Let's visualize the bar plot for the purpose and again using                            condition where paid.back.loan == No
# code starts here

df1 = df[df['paid.back.loan']=='No']

purpose_count = df1['purpose'].value_counts()

purpose_count.plot(kind='bar')
# code ends here


# --------------
# Task 5:- visualization of continuous variable
# Task Description:- Let's plot the histogram for visualization of the continuous variable. So that you will get the basic idea about how the distribution of continuous variables looks like.
# code starts here

inst_median = df['installment'].median()
print(inst_median)

inst_mean = df['installment'].mean()
print(inst_mean)

plt.hist(df['installment'])

plt.hist(df['log.annual.inc'])
# code ends here


