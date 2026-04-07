'''
Etapas do agrupamento
Dividir: primeiro, divida os dados em grupos, respeitando critérios determinados.
Aplicar: em seguida, aplique os métodos de cálculo a cada grupo para, por exemplo, encontrar o número de elementos em um grupo com o método count() ou a soma de seus valores com sum().
Combinar: por fim, os resultados são armazenados em uma nova estrutura de dados
Essas são as etapas padrão do agrupamento, e, para nossa sorte, a biblioteca pandas tem métodos prontos para cada uma delas.

Exemplo
Vamos analisar alguns dados sobre exoplanetas para ver como o agrupamento funciona na prática.

Cientistas já encontraram milhares de planetas fora do nosso sistema solar, utilizando telescópios espaciais que nos enviam imagens. Essas imagens são depois estudadas por analistas de dados. Iremos te mostrar como eles encontram planetas semelhantes à Terra.

A tabela exoplanet armazena dados de milhares de exoplanetas. Dê uma olhada nas primeiras 30 linhas:
'''
import pandas as pd

exoplanet = pd.read_csv('/datasets/exoplanets.csv')

print(exoplanet.head(30))


'''
Agrupamento em pandas
Na Pandas, agrupamos os dados usando o método groupby(), que faz o seguinte:

Assume o nome de uma coluna na qual os dados devem ser agrupados como um argumento. Este parâmetro é chamado by=. No nosso caso, vamos agrupar os dados pelo ano de descoberta.
Retorna um objeto de um tipo especial: DataFrameGroupBy. Este objeto corresponde a dados agrupados. Se você aplicar um método da biblioteca pandas nele, ele vai se transformar em uma nova estrutura de dados.
Vamos encontrar o número de exoplanetas agrupados por ano utilizando o método count():

'''

print(exoplanet.groupby(by='discovered'))
print() # vai aparecer como uma linha vazia entre duas impressões
print(exoplanet.groupby(by='discovered').count())


'''
Tarefa 1
Vamos dar mais uma olhada no nosso conjunto de dados de música e agrupá-lo de maneira semelhante à que fizemos com os exoplanetas. É importante observar que o agrupamento é geralmente executado em um conjunto de dados tratado, que não possui NaNs, duplicados ou nomes de coluna não formatados. Portanto, não usaremos o conjunto de dados music_log_raw.csv original e, em vez disso, usaremos o conjunto de dados pré-processado com todos os problemas eliminados.

A primeira etapa é agrupar o conjunto de dados por 'genre'. Quando o agrupamento for aplicado, armazene o resultado na variável genre_groups e imprima seu tipo.
'''

import pandas as pd

df = pd.read_csv('/datasets/music_log_processed.csv')

genre_groups = df.groupby(by='genre')

print(type(genre_groups))


'''
Tarefa 2
Agora vamos passar para o ambiente de aplicação e aplicar métodos computacionais a cada grupo. Lembre-se de que, eventualmente, queremos calcular o tempo total. Quando queremos encontrar o tempo total, o método que precisamos aplicar deve nos dar uma soma como resultado. Aplique ao pré-código abaixo o método apropriado (quando for adicionada, a variável genre_groups vai armazenar um DataFrame com o resultado). Quando terminar, imprima a variável genre_groups.
'''

import pandas as pd

df = pd.read_csv('/datasets/music_log_processed.csv')

genre_groups = df.groupby('genre').sum()

print(genre_groups)


'''
Tarefa 3
Nosso passo final é combinar os resultados. Não se esqueça, queremos calcular o tempo total que nossos ouvintes passaram ouvindo cada gênero. Temos uma coluna 'total_play' em nosso conjunto de dados que contém exatamente o que precisamos. Precisamos passar isso para o nosso agrupamento: primeiro, selecione a coluna e então aplique um método que calcule o tempo total.

Faça isso e imprima o resultado final.
'''

import pandas as pd

df = pd.read_csv('/datasets/music_log_processed.csv')

genre_groups = df.groupby('genre')['total_play'].sum()

print(genre_groups)