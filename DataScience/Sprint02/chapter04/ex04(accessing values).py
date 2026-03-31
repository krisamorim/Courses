import pandas as pd
import os

#código para obter o caminho completo do arquivo atual em execução 
current_dir = os.path.dirname(os.path.abspath(__file__))
#concatenar com o nome do arquivo csv para criar o caminho completo do arquivo csv
filePath = current_dir +'\\tabela_musicas.csv'

df = pd.read_csv(filePath) # reads the csv file and creates a dataframe

# print(df.head()) #shows the first 5 rows of the dataframe

# a cell
# result = df.loc[4, 'genre']
# print(result)

# a column
# print(df.loc[:, 'Artist'])


# multiple columns
# print(df.loc[:, ['Artist', 'genre']])

#Multiple consecutive columns (slice)
# print(df.loc[:, 'user_id': 'Artist'])

# a row
# print(df.loc[4, :]) #or print(df.loc[4])

# all rows starts with a specific row
# print(df.loc[1:])

#All lines, up to the specified line.
# print(df.loc[:3])

#multiple rows consecutive (slice)
# print(df.loc[2:4])

#multiple rows and columns
print(df.loc[[0,4,6], 'user_id':'Artist'])