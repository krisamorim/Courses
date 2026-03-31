import pandas as pd
import os

#código para obter o caminho completo do arquivo atual em execução 
current_dir = os.path.dirname(os.path.abspath(__file__))
#concatenar com o nome do arquivo csv para criar o caminho completo do arquivo csv
filePath = current_dir +'\\tabela_musicas.csv'

df = pd.read_csv(filePath) # reads the csv file and creates a dataframe


#extended version
# #gerar lista ssomente com genre pop
# pop_df = df[df['genre'] == 'pop']

# #filtar pop_df somente com a coluna total play
# pop_duration = pop_df['total_play']

# print(pop_duration.mean()) #calcula a média da coluna total play

#short version
print(df[df['genre'] == 'pop']['total_play'].mean()) #filtra o dataframe para obter somente as linhas onde o gênero é pop, seleciona a coluna total play e calcula a média dos valores dessa coluna.