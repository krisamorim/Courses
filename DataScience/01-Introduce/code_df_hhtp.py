import pandas as pd
import matplotlib.pyplot as plt

#clear terminal at the begining of the code
import os
os.system('cls' if os.name == 'nt' else 'clear')

#load data into a dataframe variable
df = pd.read_csv("https://raw.githubusercontent.com/alexeygrigorev/mlbookcamp-code/master/chapter-03-churn-prediction/WA_Fn-UseC_-Telco-Customer-Churn.csv") #Este dataframe se trata de um dataset de churn de clientes de telecomunicações. Objetivo: Prever qual cliente tem maior probabilidade de cancelar o serviço (churn)

# #print the first 5 rows of the dataframe and the header
# print(df.head())

# #print the first 5 rows of the dataframe and the header from the 5th column to the end
# print(df.iloc[:, 4:].head())

# #show the first 5 rows of the dataframe where data types are numeric
# print(f'The first 5 rows of the dataframe where data types are numeric:\n{df.select_dtypes(include=["number"]).head()}')

# #show the number of rows and columns in the dataframe
# print(f'This dataframe has {df.shape[0]} rows and {df.shape[1]} columns. The columns are:')

# #show the column names in the dataframe
# print(f'{df.columns}\n')

# #show the data types of each column
# print(f'The data types of each column are:\n{df.dtypes}\n')

#show first 10 rown of the MonthlyCharges column
print(df["MonthlyCharges"].head(10))

# print(df["MonthlyCharges"].hist())
plot = df["MonthlyCharges"].hist()
plt.title("Distribution of Monthly Charges")
plt.xlabel("Monthly Charges")
plt.ylabel("Frequency")
plt.show()