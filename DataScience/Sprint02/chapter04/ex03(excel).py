import pandas as pd
import os

#código para obter o caminho completo do arquivo atual em execução 
current_dir = os.path.dirname(os.path.abspath(__file__))
#concatenar com o nome do arquivo excel para criar o caminho completo do arquivo excel
excelFile = current_dir +'\\file_example_XLS_10.xls'

df_excel = pd.read_excel(excelFile) # reads the excel file and creates a dataframe

print(df_excel.head()) #shows the first 5 rows of the dataframe

# df = pd.read_csv('https://cdn.wsform.com/wp-content/uploads/2020/06/industry.csv')

# print(df.head()) #shows the first 5 rows of the dataframe
# print(df.tail(3)) # shows the last 3 rows of the dataframe
# print(df.info()) # shows information about the dataframe
# print(df.describe()) # shows descriptive statistics about the dataframe
# print(df['Industry'].value_counts()) # shows the count of each unique value in the 'Industry' column
# print(df['Industry'].unique()) # shows the unique values in the 'Industry' column
# print(df['Industry'].nunique()) # shows the number of unique values in the 'Industry' column
# print(df['Industry'].value_counts().head(3)) # shows the top 3 most frequent values in the 'Industry' column
# print(df['Industry'].value_counts().tail(3)) # shows the bottom 3 least frequent values in the 'Industry' column

