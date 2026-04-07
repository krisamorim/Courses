# #ordenar o dataframe exoplanet por raio (radius) e mostrar os 10 primeiros registros
# print(exoplanet.sort_values(by='radius').head(10))

# Aqui está o código que ordena apenas a coluna radius (raio) e imprime os 10 primeiros resultados:
# print(exoplanet['radius'].sort_values().head(10))


# filtrar todos com raio menos q 1
# depois filtrar o novo filtro para deixar somente os que foram descoberto em 2014
# e depois ordernar por raio do maior para o menor
# exo_small_14 = exoplanet[exoplanet['radius'] < 1]
# exo_small_14 = exo_small_14[exo_small_14['discovered'] == 2014]
# exo_small_14 = exo_small_14.sort_values(by='radius', ascending=False)


'''
Tarefa 1
Na lição anterior, você agrupou nossos dados music_log_processed.csv por 'genre' e calculou o tempo total que nossos ouvintes passaram ouvindo cada gênero. O resultado para cada 'genre', temos o tempo total ouvido. Ele está armazenado na variável time_by_genre no pré-código.

Agora, vamos ordenar os resultados por ordem decrescente e ver os 10 principais gêneros que nossos ouvintes mais ouviram. Faça isso e salve os resultados na variável time_by_genre_sort.

Observe que para esta tarefa, você não precisa especificar a coluna pela qual os dados precisam ser ordenados, já que há apenas uma coluna na variável time_by_genre.
'''

import pandas as pd

df = pd.read_csv('/datasets/music_log_processed.csv')

time_by_genre = df.groupby('genre')['total_play'].sum()

time_by_genre_sort = time_by_genre.sort_values(ascending=False)

print(time_by_genre_sort.head(10))