import pandas as pd
import numpy as np

df1 = pd.read_excel(r"C:\Users\User\Downloads\chrunk\data\CustomerChurn.xlsx")
df2 = pd.read_excel(r"C:\Users\User\Downloads\chrunk\data\Telco_customer_churn.xlsx")
df3 = pd.read_excel(r"C:\Users\User\Downloads\chrunk\data\Telco_customer_churn_demographics.xlsx")
df4 = pd.read_excel(r"C:\Users\User\Downloads\chrunk\data\Telco_customer_churn_location.xlsx")
df5 = pd.read_excel(r"C:\Users\User\Downloads\chrunk\data\Telco_customer_churn_population.xlsx")
df6 = pd.read_excel(r"C:\Users\User\Downloads\chrunk\data\Telco_customer_churn_services.xlsx")
df7 = pd.read_excel(r"C:\Users\User\Downloads\chrunk\data\Telco_customer_churn_status.xlsx")

"""print(df1.head())
print(df2.head())
print(df3.head())
print(df4.head())
print(df5.head())
print(df6.head())
print(df7.head())"""

df1.isna().sum()


