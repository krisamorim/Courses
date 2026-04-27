#troubleshooting
# 1. Identify the delimeter (Although the file is a CSV, the delimiter is not always a comma, so identify the delimiter.)
# use the .head() method to check the first few rows of the file and identify the delimiter. For example, if the file is tab-delimited, you will see that the values are separated by tabs instead of commas.
# Use the sep= parameter so that the file import uses a different separator.

# → no parameter:
#   Afghanistan|Kajaki Hydroelectric Power Plant Afghanistan|33   0|32   322|65   119|Hydro|
# 0                                 Afghanistan|Kandahar DOG|10   0|31    67|65   795|Solar|
# 1                                 Afghanistan|Kandahar JOL|10   0|31   623|65   792|Solar|
# 2           Afghanistan|Mahipar Hydroelectric Power Plant ...   0|34   556|69  4787|Hydro|
# 3           Afghanistan|Naghlu Dam Hydroelectric Power Pla...   0|34   641|69   717|Hydro|
# 4           Afghanistan|Nangarhar (Darunta) Hydroelectric ...  55|34  4847|70  3633|Hydro|

# → using sep parameter: data = pd.read_csv('/datasets/gpp_modified.csv', sep='|')
#   Afghanistan       Kajaki Hydroelectric Power Plant Afghanistan   33,0   32,322   65,119  Hydro  Unnamed: 6
# 0  Afghanistan                                       Kandahar DOG   10,0    31,67   65,795  Solar         NaN
# 1  Afghanistan                                       Kandahar JOL   10,0   31,623   65,792  Solar         NaN
# 2  Afghanistan      Mahipar Hydroelectric Power Plant Afghanistan   66,0   34,556  69,4787  Hydro         NaN
# 3  Afghanistan   Naghlu Dam Hydroelectric Power Plant Afghanistan  100,0   34,641   69,717  Hydro         NaN
# 4  Afghanistan  Nangarhar (Darunta) Hydroelectric Power Plant ...  11,55  34,4847  70,3633  Hydro         NaN

# 2. handling the header

# → using header and name parameter
# header= None: this tells pandas that the file does not have a header row, so it will not treat the first row as column names.
# e.g.: data = pd.read_csv('/datasets/gpp_modified.csv', sep='|', header=None)

# → using name parameter: this allows you to specify the column names manually. You can provide a list of column names that correspond to the columns in the file.
# e.g.: 
# column_names = [
#     'country',
#     'name',
#     'capacity_mw',
#     'latitude',
#     'longitude',
#     'primary_fuel',
#     'owner'
# ]
# data = pd.read_csv('/datasets/gpp_modified.csv', sep='|', header=None, names=column_names)

# 3. handling supended points
# on read_csv() period is standard, lets use the dacimal parameter to specify that the decimal separator is a comma instead of a period.
# e.g.: data = pd.read_csv('/datasets/gpp_modified.csv', sep='|', header=None, names=column_names, decimal=',')

# 4. handling excel files
# reading first sheet: df = pd.read_excel('/datasets/product_reviews.xlsx')
# reading other sheet: df = pd.read_excel('/datasets/product_reviews.xlsx', sheet_name='reviewers') #using parameter sheet_name to specify the sheet to read. You can provide the name of the sheet or its index (starting from 0).
# P. S. we can also use index to specify the sheet: df = pd.read_excel('/datasets/product_reviews.xlsx', sheet_name=0) #this will read the first sheet, which is the default behavior of read_excel().

# -------------------------------------------------------------------------------------------
# TAREFA1
# import pandas as pd
# df_reviews = pd.reade_excel('/datasets/product_reviews.xlsx')

# #calcular o valor médio da coluna review em df_reviews
# average_review = df_reviews['review'].mean()
# -------------------------------------------------------------------------------------------

# # TAREFA2
# import pandas as pd

# df_products = pd.read_excel('/datasets/product_reviews.xlsx', sheet_name='products')

# #classifique o DataFrame pela coluna 'id' em ORDEM DECRESCENTE usando o método apropriado e armazene-o na variável sorted_df_products
# sorted_df_products = df_products.sort_values(by='id', ascending=False)

# 5. Método info()
# Número de linhas (RangeIndex: 34936 entries)
# Número de colunas (total 7 columns)
# Nome de cada coluna (Column)
# Número de valores em cada coluna que não estão ausentes (Non-Null Count)
# Tipo de dados de cada coluna (Dtype)

# 6. handling shape()
# retur a tuple
# use o data.shape() para obter dados sobre s tabela e armazenar em variáveis
# Ex: n_rows, n_cols = data.shape
#

# 7. sample()
# Ao contrário de head() e tail(), sample() seleciona 1 linha por padrão, E o resultado mudará cada vez que você executar o código. Isso porque sample() seleciona as linhas "aleatoriamente", mas você pode especificar o número de linhas que deseja selecionar usando o parâmetro n. Por exemplo, data.sample(n=5) selecionará 5 linhas aleatórias do DataFrame.

# Se você quiser usar sample() e sempre obter o mesmo resultado ao executar o código, precisará usar o parâmetro random_state= e configurá-lo para algum valor inteiro de sua escolha (qualquer número inteiro entre 0 e 4294967295). Aqui está um exemplo:
#e.g: print(data.sample(5, random_state=1369))

#--------------------------------------------------------------------------------------------
#Tarefa 1
'''
O pré-código já inclui código para imprimir as primeiras 5 linhas do conjunto de dados de usinas usando o método head(). Escreva um código que:

tenha uma amostra de 5 linhas aleatórias do conjunto de dados e as armazene na variável sample. Use random_state=543210 para a amostragem.
imprima a variável sample.

import pandas as pd

column_names = [
    'country',
    'name',
    'capacity_mw',
    'latitude',
    'longitude',
    'primary_fuel',
    'owner'
]
data = pd.read_csv(
    '/datasets/gpp_modified.csv',
    sep='|',
    header=None,
    names=column_names,
    decimal=',',
)

print(data.head())
print()

sample = data.sample(5, random_state=543210)
print(sample)

'''
#--------------------------------------------------------------------------------------------

# 8. Handling describe()
# O método describe() é usado para obter uma visão geral estatística de um DataFrame. Ele retorna várias estatísticas descritivas para cada coluna numérica do DataFrame, como contagem, média, desvio padrão, valor mínimo, percentis e valor máximo. Essas estatísticas podem ser úteis para entender a distribuição dos dados e identificar possíveis outliers ou tendências.

'''
TAREFA 1

import pandas as pd

column_names = [
    'country',
    'name',
    'capacity_mw',
    'latitude',
    'longitude',
    'primary_fuel',
    'owner'
]
data = pd.read_csv(
    '/datasets/gpp_modified.csv',
    sep='|',
    header=None,
    names=column_names,
    decimal=',',
)

1- basedo no código acima Obtenha uma visão geral apenas da coluna 'primary_fuel' chamando describe() nela e imprimindo o resultado.
Resposta: print(data['primary_fuel'].describe())

2- No resultado da tarefa anterior, descobrimos que existem 15 valores únicos na coluna 'primary_fuel'. Vamos verificar isso agora. Para fazer isso, chame o método nunique() nessa coluna. Atribua o resultado a uma variável chamada unique e imprima-a na tela.
Resposta: 
unique = data['primary_fuel'].nunique()
print(unique)

3.Agora verifique se o valor mais comum na coluna 'primary_fuel' realmente é 'Solar'. Para fazer isso:

3.1Filtre o DataFrame original, extraindo apenas as linhas em que 'primary_fuel' é igual a 'Solar' e armazene-o na variável solar_data.
solar_data = data[data['primary_fuel'] == 'Solar']
3.2Verifique a forma do DataFrame obtido e o armazene na variável solar_shape.
solar_shape = solar_data.shape
3.3Imprima a variável.

'''


#Tratamento de valores ausentes e duplicados
# 1. Verificando valores ausentes
# df.isna().sum() ou df.isnull().sum()

#outra forma é utilizando value_counts() para verificar a contagem de cada valor único em uma coluna. Se houver valores ausentes, eles aparecerão como NaN ou None na contagem.
# Ex: df_logs['source'].value_counts(dropna=False)
# Ex2: df_logs['source'].value_counts(dropna=False).sort_index()) #caso queira em ordem alfabética da coluna do nome do valores

# -------------------------------------------------------------------------------------------------
# TAREFA 1
'''
Tarefa 2
Agora vamos tentar ordenar os resultados por índice, e não por valor, para ver se isso acrescenta algum significado aos valores da coluna 'email'. Reescreva a variável email_values usando a ordenação e imprima o resultado.
'''