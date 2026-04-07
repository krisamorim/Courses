import pandas as pd

rating = ['date', 'name', 'points']
players = [
    ['2018.01.01',  'Rafael Nadal', 10645],
    ['2018.01.08',  'Rafael Nadal', 10600],
    ['2018.01.29',  'Rafael Nadal', 9760],
    ['2018.02.19',  'Roger Federer', 10105], 
    ['2018.03.05',  'Roger Federer', 10060],
    ['2018.03.19',  'Roger Federerr', 9660],
    ['2018.04.02',  'Rafael Nadal Parera', 8770],
    ['2018.06.18',  'Roger Fedrer', 8920],
    ['2018.06.25',  'Rafael Nadal Parera', 8770],
    ['2018.07.16',  'Rafael Nadal Parera', 9310],
    ['2018.08.13',  'Rafael Nadal Parera', 10220],
    ['2018.08.20',  'Rafael Nadal Parera', 10040],
    ['2018.09.10',  'Rafael Nadal Parera', 8760],
    ['2018.10.08',  'Rafael Nadal Parera', 8260],
    ['2018.10.15',  'Rafael Nadal Parera', 7660],
    ['2018.11.05',  'Novak Djokovic', 8045],
    ['2018.11.19',  'Novak Djokovic', 9045]
]
tennis = pd.DataFrame(data=players, columns=rating)
# print(tennis)
# print(tennis['name'].unique())
# print(tennis['name'].nunique())

tennis['name'].replace('Roger Federerr', 'Roger Federer', inplace = True)
tennis['name'].replace('Roger Fedrer', 'Roger Federer', inplace = True)
tennis['name'].replace('Rafael Nadal', 'Rafael Nadal Parera', inplace = True)

print(tennis)


'''
Tarefa 3
Chegou a hora de verificar o número de valores únicos na coluna 'Artist'. Armazene os valores únicos na variável pop_artists. O número de artistas únicos deve ser posto na variável n_artists. Imprima ambas as variáveis.
'''

import pandas as pd

df = pd.read_csv('/datasets/music_log_raw.csv')

pop = df[df['genre'] == 'pop']

pop_artists = pop['Artist'].unique()
n_artists = pop['Artist'].nunique()

print(pop_artists)
print(n_artists)