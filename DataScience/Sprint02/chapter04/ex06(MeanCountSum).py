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
# print(df[df['genre'] == 'pop']['total_play'].mean()) #filtra o dataframe para obter somente as linhas onde o gênero é pop, seleciona a coluna total play e calcula a média dos valores dessa coluna.

'''
Tarefa 1
Em cenários da vida real, as empresas costumam ter perguntas específicas que exigem respostas. Por exemplo, uma empresa talvez precise analisar os dados de um usuário específico com o 'user_id' igual a '5D9AAD37'.

Vamos fazer isso agora. Para conseguir isso, você precisa filtrar a tabela para extrair apenas as linhas relevantes para o usuário ('5D9AAD37'). Em seguida, pediremos que você calcule a duração média das músicas que esse usuário reproduziu. Essas informações são armazenadas na coluna 'total play'. Após calcular, armazene os resultados na variável user_mean_dur e a imprima.'''


# df = pd.read_csv('/datasets/music_log_chpt_11.csv')
# user_mean_dur = df[df['user_id'] == '5D9AAD37']['total play'].mean()
# print(user_mean_dur)


#O método count()

# Por exemplo, podemos usar ele para calcular o número de músicas que os usuários ouviram por mais de 3 minutos (180 segundos). 

df = pd.read_csv('/datasets/music_log_chpt_11.csv')
duration_threshold = 180
long_songs = df[df['total play'] > duration_threshold]['total play'].count()
print(long_songs)

'''Escreva o código para contar o número de músicas para as quais 'Aura' é o artista. Você vai precisar da coluna 'Artist' para fazer isso. Armazene o resultado na variável aura_count. Não se esqueça de imprimir este número.'''
artist = 'Aura'
aura_count = df[df['Artist'] == artist]['Artist'].count()
print(aura_count)


# o método sum() é usado para calcular a soma dos valores em uma coluna. Por exemplo, podemos usá-lo para calcular o total de tempo gasto ouvindo músicas de um artista específico.

'''Tarefa 3
Escreva código para calcular o número total de segundos que nossos usuários ouviram as músicas do artista 'Zodiac'. Armazene o resultado na variável zodiac_total e imprima-o.'''

# zodiac_total = df[df['Artist'] == 'Zodiac']['total play'].sum()


#TARFA FINAL
'''Crie uma lista de listas intituladas state_animals. Cada lista contém dois valores string: o nome de um estado e seu animal correspondente. A lista state_animals deve ter dez elementos.

Em seguida, crie uma lista chamada col_names com dois elementos: os nomes das colunas 'state' e 'animal'.

A etapa final é criar um DataFrame com state_animals como valores e col_names como nomes das colunas. Armazene este DataFrame na variável df e imprima-o.

'Alabama' — 'black bear'
'Alaska' — 'moose'
'Arizona' — 'ringtail'
'Arkansas' — 'white-tailed deer'
'California' — 'grizzly bear'
'Colorado' — 'rocky Mt. bighorn sheep'
'Connecticut' — 'sperm whale'
'Delaware' — 'gray fox'
'Florida' — 'manatee'
'Georgia' — 'white-tailed deer'
'''

# import pandas as pd

# state_animals= [
#   ['Alabama', 'black bear'],
#   ['Alaska', 'moose'],
#   ['Arizona', 'ringtail'],
#   ['Arkansas', 'white-tailed deer'],
#   ['California', 'grizzly bear'],
#   ['Colorado', 'rocky Mt. bighorn sheep'],
#   ['Connecticut', 'sperm whale'],
#   ['Delaware', 'gray fox'],
#   ['Florida', 'manatee'],
#   ['Georgia', 'white-tailed deer']
# ]

# col_names = ['state', 'animal']

# df = pd.DataFrame(data=state_animals, columns=col_names)

# print(df)


'''Vamos praticar a indexação do DataFrame usando o conjunto de dados music_log_chpt_11.csv que vimos antes. Seu objetivo é usar a notação .loc[] para extrair as linhas 2 a 600 para as colunas do DataFrame Artist e track. Armazene a fatia extraída na variável sliced e imprima-a.'''

import pandas as pd

df = pd.read_csv('/datasets/music_log_chpt_11.csv')

sliced = df.loc[1:599][['Artist', 'track']] # Escreva seu código aqui

print(sliced)



'''Anteriormente você extraiu as linhas 2 a 600 para as colunas Artist e track do DataFrame e armazenou o resultado na variável sliced. Agora vamos filtrar este DataFrame usando indexação lógica para obter apenas as linhas onde o 'Artist' é 'Griffin & Flint'. Armazene o DataFrame filtrado na variável griffin_flint e imprima-o.'''

import pandas as pd

df = pd.read_csv('/datasets/music_log_chpt_11.csv')

sliced = df.loc[1:599, ['Artist', 'track']]

griffin_flint = sliced[(sliced['Artist'] == 'Griffin & Flint')]

print(griffin_flint)


'''Agora vamos praticar alguns dos métodos mais comuns usados com DataFrames. Anteriormente você filtrou o DataFrame usando indexação lógica e obteve linhas onde 'Artist' é 'Griffin & Flint'. Agora você deseja contar o número de linhas obtidas. Para fazer isso aplique o método apropriado, armazene a contagem na variável count e imprima seu valor.'''

import pandas as pd

df = pd.read_csv('/datasets/music_log_chpt_11.csv')

sliced = df.loc[1:599, ['Artist', 'track']] 

griffin_flint = sliced[sliced['Artist'] == 'Griffin & Flint']

count = griffin_flint['Artist'].count()

print(count)