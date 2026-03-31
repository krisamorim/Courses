import pandas as pd
import os

#código para obter o caminho completo do arquivo atual em execução 
current_dir = os.path.dirname(os.path.abspath(__file__))
#concatenar com o nome do arquivo csv para criar o caminho completo do arquivo csv
filePath = current_dir +'\\tabela_musicas.csv'

df = pd.read_csv(filePath) # reads the csv file and creates a dataframe

# print(df['genre'] == 'pop')  #same: print(df.loc[:, 'genre'] == 'pop')

# print(df.loc[:, 'genre'] == 'pop')

# print(df.loc[df.loc[:, 'genre'] == 'pop']) # same: print(df[df['genre'] == 'pop'])



'''
Tarefa 1
Vamos praticar um pouco agora.

Use a indexação lógica para filtrar o DataFrame armazenado na variável df. A tabela resultante deve conter apenas linhas com 'genre' igual a 'jazz'. Armazene a tabela filtrada na variável jazz_df e imprima-a.'''

# jazz_df = df[df['genre'] == 'jazz']
# print(jazz_df)

'''
Tarefa 2
Agora vamos usar a indexação lógica para filtrar o DataFrame novamente. Filtre a tabela original para incluir apenas as músicas com 'total play' superior a 90 segundos. Armazene a tabela filtrada na variável high_total_play_df e imprima-a.
'''

# high_total_play_df = df[df['total play'] > 90]

# print(high_total_play_df)

'''A propósito, podemos aplicar várias condições primeiro aplicando a primeira condição e armazenando o resultado. Então, podemos chamar a indexação lógica com a segunda condição. Veja o exemplo abaixo e execute o código para verificar a saída.'''

# # selecionando linhas em que o gênero é jazz e total play varia entre 80 e 130
# df = df[df['total play'] >= 80]
# df = df[df['total play'] <= 130]
# df = df[df['genre'] == 'jazz']

# print(df)