# --------------
# Import packages
import numpy as np
import pandas as pd
from scipy.stats import mode 
 



# code starts her
bank = pd.read_csv('/opt/greyatom/kernel-gateway/data/executor/attachments/account/b1/2a7f53f8-19f6-45c7-9d74-560da9338b1a/b69/a340d73b-3d57-4e25-9cfd-074cea5af958/file.csv')
bank.head()
categorical_var = bank.select_dtypes(include = 'object')
print(categorical_var)
numerical_var = bank.select_dtypes(include = 'number')
print(numerical_var)
# code ends here


# --------------
# code starts here
bank.head()
banks = bank.drop(['Loan_ID'], axis=1)
#print(banks)
a = banks.isnull().sum()
#print(a)
bank_mode = banks.mode()
#print(bank_mode)
banks = banks.fillna(bank_mode.iloc[0])
print(banks)
#code ends here


# --------------
# Code starts here
avg_loan_amount = pd.pivot_table(banks,index=['Gender','Married','Self_Employed'],values='LoanAmount',aggfunc='mean')
print(avg_loan_amount)


# code ends here



# --------------
# code starts here
banks.head()
df1 = banks['Self_Employed']== 'Yes'
#print(df1)
df2 = banks['Self_Employed']== 'No'
#print(df2)
df3 = banks['Loan_Status'] == 'Y'
loan_approved_se = len(banks[df1 & df3])
loan_approved_nse = len(banks[df3 & df2])
percentage_se = loan_approved_se * 100 / 614
print(percentage_se)
percentage_nse = loan_approved_nse * 100 / 614
print(percentage_nse)
# code ends here


# --------------
# code starts here
loan_term = banks['Loan_Amount_Term'].apply(lambda x: x/12)
big_loan_term = banks.loc[loan_term>=25].shape[0]



# code ends here


# --------------
# code ends here
loan_groupby = banks.groupby(['Loan_Status'])['ApplicantIncome','Credit_History']
mean_values = loan_groupby.mean()



# code ends here


