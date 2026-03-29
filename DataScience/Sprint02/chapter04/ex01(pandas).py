df = []

df.shape #verificar seu tamanho

rows = df.shape[0] #número de linhas
columns = df.shape[1] #número de colunas

#outra forma de verificar o número de linhas e colunas
rows, columns = df.shape

#ver tipo de dados
df.dtypes

#ver coluna
df.columns

df.info() #ver informações gerais do DataFrame, incluindo o número de entradas, colunas, tipos de dados e uso de memória.

