# Task 1:- Loan Status
# Task Description:- Let's start with the simple task of visualizing the company's record with respect to loan approvals.

#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Code starts here
data = pd.read_csv(path)
loan_status = data['Loan_Status'].value_counts()
loan_status.plot(kind='bar')

# Task 2:- Everyone needs money
# Task Description:- The company provides financial assistance across the different regions of the country. 
#                     One interesting statistic that stakeholders want to see is the loan approval distribution across the regions.
# Things to ponder upon :- 
#                          Which is the region with the highest no. of loan approvals? lowest no. of loan approvals?
#                          Which is the region with the maximum difference between loan a
#Code starts here

property_and_loan = data.groupby(['Property_Area','Loan_Status'])
property_and_loan = property_and_loan.size().unstack()
property_and_loan.plot(kind='bar',stacked=False,figsize=(15,10))
plt.xlabel('Area')
plt.ylabel('Loan Status')
plt.xticks(rotation=45)

# Task 3:- Expensive Education
# Task Description:- Higher education has always been an expensive endeavour for people but it results in better career opportunities and stability in life. 
#                    But does higher education result in a better guarantee in issuing loans?
# Things to ponder upon :-
#                         Overall which group has asked for higher loan services irrespective of the approval? Graduate or Non Graduate?
#                         Which group has had better approval to non approval ratio? Graduate or Non Graduate?
#                         Do the above conclusions make sense? Why?
#Code starts here

education_and_loan = data.groupby(['Education','Loan_Status']).size().unstack()
education_and_loan.plot(kind='bar',stacked=True)
plt.xlabel('Education Status')
plt.ylabel('Loan Status')
plt.xticks(rotation=45)

# Task 4:- Smarter and Richer?
# Task Description:- After seeing the loan status distribution, let's check whether being graduate or not also leads to different loan amount distribution by plotting an overlapping density plot of two values
# Things to ponder upon:-
#                         Do Graduate people get approved a higher amount than their Non Graduate counterparts?
#                         What's the average amount of loan approved for Graduate? for Non Graduate? Is there a huge difference between the two? 
#Code starts here

graduate = data[data['Education']=='Graduate']
not_graduate = data[data['Education']=='Not Graduate']
graduate['LoanAmount'].plot(kind='density',label='Graduate')
not_graduate['LoanAmount'].plot(kind='density',label='Not Graduate')
#For automatic legend display
plt.legend()

# Code ends here

# Task 5:- Income vs Loan
# Task Description:- For any finance institiution to be successful in it's loan lending system, there has to be a 
#                    correlation between the borrower's income and loan amount he is lent. 
#                    Let's see how our company fares in that respect:
# Things to ponder upon:-
#                         Is there a correlation between 'ApplicantIncome' and 'LoanAmount'?
#                         (One way to know that is look at the line formed when you connect the scatter plot dots?)
#                         Is the 'TotalIncome' better related to th
#Code starts here

fig,(ax_1,ax_2,ax_3)= plt.subplots(3,1,figsize=(15,15))

data.plot.scatter(x='ApplicantIncome',y='LoanAmount',ax=ax_1)
ax_1.set_title('Applicant Income')

data.plot.scatter(x='CoapplicantIncome',y='LoanAmount',ax=ax_2)
ax_2.set_title('Coapplicant Income')

data['TotalIncome']=data['ApplicantIncome']+data['CoapplicantIncome']
print(data['TotalIncome'])

data.plot.scatter(x='TotalIncome',y='LoanAmount',ax=ax_3)
ax_3.set_title('Total Income')

