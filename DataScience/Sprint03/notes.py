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

# -------------------------------------------------------------------------------------------------
#TAREFA 2
'''
Determinamos anteriormente que a coluna 'email' tem 13.953 valores não ausentes. Isso significa que mais de 90% dos dados estão ausentes! Filtre o DataFrame df_logs para que ele contenha apenas linhas onde não existam valores ausentes na coluna 'email'. Atribua os resultados filtrados a uma variável chamada df_emails, depois imprima as primeiras 10 linhas.

Para verificar se uma condição não é verdadeira ao filtrar um DataFrame, use o caractere ~ antes da condição (por exemplo, df[~df.method()]).

import pandas as pd

df_logs = pd.read_csv('/datasets/visit_log.csv')

df_emails = df_logs[~df_logs['email'].isna()]
print(df_emails.head(10))

'''
# -------------------------------------------------------------------------------------------------
#TAREFA 3
'''

A coluna 'source' mostra que muitas dessas visitas têm origem dos links de e-mails de marketing. No entanto, existem alguns valores NaN. Pode ser que visitas com endereços de e-mail, mas sem o valor de 'source', também sejam de links dos e-mails de marketing, porém a fonte não foi salva.

Verifique se há alguma linha em que ambas as colunas 'source' e 'email' têm valores ausentes. Se não houver nenhuma linha em que ambas as condições sejam verdadeiras, isso é um sinal de que os valores ausentes na coluna 'source' deveriam ser 'email'.

Para isso, filtre df_logs com a condição de que ambas as colunas 'email' e 'source' tenham valores ausentes. Atribua o resultado para uma variável chamada df_emails e a imprima.

import pandas as pd

df_logs = pd.read_csv('/datasets/visit_log.csv')

df_emails = df_logs[df_logs['email'].isna() & df_logs['source'].isna()]

print(df_emails)

'''
# -------------------------------------------------------------------------------------------------

#Variáveis quantitativas e categóricas
'''
As variáveis quantitativas têm valores numéricos que podemos usar para cálculos aritméticos. Coisas como altura, peso, idade e receita são exemplos de variáveis quantitativas. Em Python, essas grandezas costumam ser armazenadas como números inteiros ou de ponto flutuante.

Já as variáveis categóricas representam um conjunto de valores possíveis que uma observação específica pode ter. Coisas como cor, marca e modelo de um carro são exemplos de variáveis categóricas. Em Python, elas costumam ser armazenadas como strings, mas também podem ser valores booleanos ou até mesmo números inteiros.

Exemplos de valores inteiros categóricos são códigos postais ou rótulos numéricos que representam outros valores (por exemplo, 1 = vermelho, 2 = azul, etc.) De qualquer forma, não faz sentido realizar operações aritméticas com valores categóricos.

'''

#Preenchimento de valores categóricos ausentes
# -------------------------------------------------------------------------------------------------
#TAREFA 1
'''
Use replace() para substituir os valores ausentes na coluna 'source' pela string 'email'.
Verifique o seu trabalho chamando o método unique() na coluna 'source' e imprimindo os resultados.

import pandas as pd

df_logs = pd.read_csv('/datasets/visit_log.csv', keep_default_na=False)

df_logs['source'] = df_logs['source'].replace('', 'email')

print(df_logs['source'].unique())

'''
# -------------------------------------------------------------------------------------------------

#Tarefa 2
'''
Para calcular a taxa de conversão de cada fonte de tráfego, primeiro determine quantas visitas de cada fonte existem.

Para encontrar o número total de visitas de cada fonte de tráfego, use groupby() para agrupar dados pela coluna 'source', depois conte o número de valores na coluna 'user_id' do DataFrame agrupado. Atribua o resultado à variável visits e a imprima.

O pré-código já contém o que você fez para preencher os valores ausentes.
import pandas as pd

df_logs = pd.read_csv('/datasets/visit_log.csv', keep_default_na=False)
df_logs['source'] = df_logs['source'].replace('', 'email')

visits = df_logs.groupby('source')['user_id'].count()
print(visits)
'''
# -------------------------------------------------------------------------------------------------

#Tarefa 3
'''
A seguir, determine o número de visitas em que uma compra foi feita para cada fonte, calculando a soma da coluna 'purchase' para cada agrupamento de fonte. Depois disso, atribua os resultados à variável purchases e a imprima.
import pandas as pd

df_logs = pd.read_csv('/datasets/visit_log.csv', keep_default_na=False)
df_logs['source'] = df_logs['source'].replace('', 'email')

purchases = df_logs.groupby('source')['purchase'].sum()
print(purchases)
'''
# -------------------------------------------------------------------------------------------------

#Tarefa 4
'''
Calcule a taxa de conversão de cada fonte de tráfego, salve os resultados em conversion e a imprima. A taxa de conversão é a proporção de visitas em que uma compra foi feita. O pré-código tem as visitas e compras do exercício anterior.
import pandas as pd

df_logs = pd.read_csv('/datasets/visit_log.csv', keep_default_na=False)
df_logs['source'] = df_logs['source'].replace('', 'email')

visits = df_logs.groupby('source')['user_id'].count()
purchases = df_logs.groupby('source')['purchase'].sum()

conversion = purchases / visits
print(conversion)
'''
# -------------------------------------------------------------------------------------------------

# mean() e median() 
# são medidas de tendência central que podem ser usadas para resumir um conjunto de dados. A média é a soma de todos os valores dividida pelo número total de valores, enquanto a mediana é o valor do meio quando os dados estão ordenados. A média é sensível a valores extremos (outliers), enquanto a mediana é mais robusta a eles. Portanto, a escolha entre média e mediana depende da distribuição dos dados e da presença de outliers. Se os dados forem simétricos e não tiverem outliers, a média pode ser uma boa escolha. Se os dados forem assimétricos ou tiverem outliers, a mediana pode ser uma melhor representação do valor típico.


#TAREFA 1
'''
Calcular a idade média e a salvamos em uma variável chamada age_avg, depois a usamos para preencher os valores ausentes em 'age':
import pandas as pd

analytics_data = pd.read_csv('/datasets/web_analytics_data.csv')

age_avg = analytics_data['age'].mean()
print("Idade média:", age_avg)

analytics_data['age'] = analytics_data['age'].fillna(age_avg)
'''

#-------------------------------------------------------------------------------------------------
#TAREFA 2
'''
Comece dividindo os dados em dois DataFrames: um para visitas vindas de desktops e outro para visitas de dispositivos móveis. Atribua as visitas de desktop a uma variável chamada desktop_data e as visitas de aparelhos móveis a outra chamada mobile_data.

import pandas as pd

analytics_data = pd.read_csv('/datasets/web_analytics_data.csv')

age_avg = analytics_data['age'].mean()
analytics_data['age'] = analytics_data['age'].fillna(age_avg)

desktop_data = analytics_data[analytics_data['device_type'] == 'desktop']
mobile_data = analytics_data[analytics_data['device_type'] == 'mobile']
'''

#-------------------------------------------------------------------------------------------------
#TAREFA 3
'''
Use o tempo médio das visitas de desktop para preencher os valores ausentes da coluna 'time' de desktop_data e a média de tempo de visita de dispositivos móveis para preenchê-los em mobile_data.

desktop_avg = desktop_data['time'].mean()
mobile_avg = mobile_data['time'].mean()

Resposta:
desktop_data['time'] = desktop_data['time'].fillna(desktop_avg)
mobile_data['time'] = mobile_data['time'].fillna(mobile_avg)
'''

#DUPLICIDADE
'''
Precisamos ter a capacidade de analisar o conjunto de dados de uma só vez.
1.	VERIFICAR DUPLICIDADE
→ Verificar duplicidade com duplicated(): usar o método duplicated() com sum() para obter o número de valores duplicados em uma única coluna ou linhas duplicadas em um DataFrame
→ Verificar duplicidade com value_counts(): Esse método identifica todos os valores unívocos em uma coluna e calcula quantas vezes cada um aparece. Você pode aplicar esse método a um objeto Series para obter pares valor-frequência em ordem decrescente. As entradas mais frequentemente duplicadas podem ser encontradas no topo da lista.

2.  Converter tudo em minúsculoa (Você deve ter certeza de que a caixa alta das letras não é importante antes de transformar todas as strings em letras minúsculas.)
import pandas as pd
df = pd.DataFrame({'col_1': ['A', 'B', 'A', 'A'], 'col_2': [1, 2, 2, 1]})
df['col_1'] = df['col_1'].str.lower()

3. Mudar uma palavra específica nas linahs de uma coluna especifica
df = pd.read_csv('/datasets/file.csv')
df['NomeDaColuna'] = df['NomeDaColuna'].str.replace('Palavra no arquivo', 'palavra nova')

4. SAlvar resultado em nova coluna
Pode manter a coluna original e criar uma coluna adicional onde as strings foram modificadas. Por exemplo, você pode salvar o resultado da substituição feita na coluna 'item' em uma nova coluna chamada 'item_modified'
df = pd.read_csv('/datasets/file.csv')
df['column_modified'] = df['column_name'].str.replace('Old_Word', 'new_word')

REMOVER DUPLICIDADE:
Utilizar drop_duplicates()
'''
#----------------------------------------------------------------------------------------------------------------------------------------------------------
'''
Tarefa 1
Transforme os nomes dos modelos de celulares em letras minúsculas usando o método str.lower() e salve-os em uma nova coluna chamada 'item_lowercase', mas mantenha a coluna original 'item'.
Imprima as primeiras linhas da tabela atualizada e veja o que acontece.



df_stock = pd.read_csv('/datasets/phone_stock.csv')

df_stock['item_lowercase'] = df_stock['item'].str.lower()

print(df_stock.head())
'''
#----------------------------------------------------------------------------------------------------------------------------------------------------------

'''
Tarefa 2
Usando sua coluna recém-criada 'item_lowercase' e o método sum(), calcule o número total dos dois modelos de celulares:

'apple iphone xr 64gb'
'samsung galaxy a30 32gb'
Para contar o número de modelos de celulares Apple, filtre o DataFrame com base na coluna 'item_lowercase' para incluir apenas as linhas com 'apple iphone xr 64gb' como o valor. Em seguida, extraia a coluna 'count' do DataFrame filtrado e aplique o método sum() a ela. Armazene o número total de celulares Apple na variável apple.

Para celulares Samsung, siga o mesmo procedimento, com a única diferença sendo que o número total de celulares Samsung deve ser salvo na variável samsung.



import pandas as pd

df_stock = pd.read_csv('/datasets/phone_stock.csv')
df_stock['item_lowercase'] = df_stock['item'].str.lower()

apple = df_stock[df_stock['item_lowercase'] == 'apple iphone xr 64gb']['count'].sum()
samsung = df_stock[df_stock['item_lowercase'] == 'samsung galaxy a30 32gb']['count'].sum()

print("Número total de celulares Apple:", apple)
print("Número total de celulares Samsung:", samsung)
O pré-código já contém código para imprimir os resultados, então não o modifique.
'''

#----------------------------------------------------------------------------------------------------------------------------------------------------------
'''
Tarefa 3
Agora exclua as linhas com celulares duplicados chamando drop_duplicates() em df_stock. Precisamos excluir linhas com base apenas na coluna item_lowercase, então certifique-se de usar esse nome como valor para o parâmetro subset=.

Lembre-se de que, depois de remover duplicados, precisamos chamar o método reset_index() com o parâmetro drop=True. Isso nos permite corrigir a indexação e remover o índice antigo.

A propósito, você pode fazer tudo isso em apenas uma linha de código! Pode ser um pouco desafiador, mas pense em como pode fazer isso.

Seu resultado final deve ser atribuído de volta a df_stock. Imprima as primeiras linhas de df_stock quando terminar.
import pandas as pd

df_stock = pd.read_csv('/datasets/phone_stock.csv')
df_stock['item_lowercase'] = df_stock['item'].str.lower()

df_stock = df_stock.drop_duplicates(subset=['item_lowercase']).reset_index(drop=True)
print(df_stock.head())

'''

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''
Tarefa 4
Vamos fazer algo muito legal! Não se preocupe, você tem tudo que precisa para isso, e nós vamos ajudar.

O pré-código inclui uma linha que você escreveu anteriormente para se livrar de duplicados, então agora temos o DataFrame df_stock sem duplicados. Seu objetivo é definir os valores corretos na coluna 'count' para as linhas em que 'item' é 'Apple iPhone XR 64GB' e 'Samsung Galaxy A30 32GB'.

Os valores que você vai definir já foram calculados anteriormente e estão armazenados nas variáveis apple e samsung no pré-código.

A melhor maneira de atualizar os valores na coluna 'count' é usar o atributo loc[], que pode substituir os valores em um determinado lugar.

Vamos dar uma olhada em df_stock após a remoção de duplicados para ilustrar como loc[] pode nos ajudar a atualizar valores:

Para atualizar o valor na primeira linha (índice 0) e a coluna count' para o modelo Apple iPhone, podemos usar loc[]. Passamos dois valores para loc[] para especificar o índice da linha e o nome da coluna e, em seguida, usamos o sinal = para definir o valor desejado:
exemplo: df_stock.loc[0,'count'] = 33

No exemplo anterior, o valor 33 foi definido, mas nós queremos definir o valor da variável apple que anteriormente calculamos e salvamos.

Esse foi um exemplo para Apple iPhone. Para Samsung, o procedimento é o mesmo, exceto que passamos diferentes valores para o atributo loc[].


import pandas as pd

df_stock = pd.read_csv('/datasets/phone_stock.csv')
df_stock['item_lowercase'] = df_stock['item'].str.lower()

apple = df_stock[df_stock['item_lowercase'] == 'apple iphone xr 64gb']['count'].sum()
samsung = df_stock[df_stock['item_lowercase'] == 'samsung galaxy a30 32gb']['count'].sum()

df_stock = df_stock.drop_duplicates(subset='item_lowercase').reset_index(drop=True)

# escreva seu código aqui (Use loc com os seguintes parâmetros: 0, 'count' )
df_stock.loc[0, 'count'] = apple
df_stock.loc[3, 'count'] = samsung
print(df_stock.head())
'''

'''
CASE
No código abaixo, lemos o conjunto e o armazenamos na variável df. Veja como ficam as primeiras linhas do conjunto de dados:
+---+------------+----------+-------+
|   | category   | product  | price |
+---+------------+----------+-------+
| 0 | cosmetics  | lipstick | 25.0  |
| 1 | cosmetics  | LIPSTIC  | 25.0  |
| 2 | tbc        | pacifier | 9.0   |
| 3 | hair care  | shampoo  | 12.0  |
| 4 | baby care  | diapers  | 34.0  |
+---+------------+----------+-------+

1º - criar dataframe
import pandas as pd
df = pd.read_csv('/datasets/products_data.csv')

2º - Conhecer o conjunto de dados
# informação geral
print(df.info())

#contagem de valores ausentes
print(df.isna().sum())

# mostrar as primeiras linhas do dataframe
print(df.head())

# mostrar 10 linhas aleatórias do dataframe
print(df.sample(10, random_state=42))

# mostrar linhas duplicadas
print(df[df.duplicated()])

3º - ao encontrar as colunas que tem  dados ausentes
# ver as através das colunas as linhas que tem dados ausentes
# Já identificamos a presença deles na coluna 'price' criando um objeto Series de valores booleanos e armazenando-o na variável mis_booleans.
mis_booleans = df['price'].isna()

# Agora use essa variável para filtrar o DataFrame original, extraindo as linhas que contêm valores ausentes, e salve o resultado da filtragem na variável mis_rows. Imprima o resultado.
mis_rows = df[mis_booleans]
print(mis_rows)

4º - preencher os valores ausentes (calcular a média e preencher os valores ausentes com a média)
# Agrupe os dados pela coluna 'category' e extraia a coluna 'price'e aplique um método apropriado para calcular o valor médio de preço de cada categoria e salve-o na variável avg_per_category.
avg_per_category = df.groupby('category')['price'].mean()

print(avg_per_category)
saida:
category
baby care    34.000000
cosmetics    22.666667
hair care    16.500000
tbc           9.000000
Name: price, dtype: float64

# Está quase tudo pronto para preencher o valor ausente. Para fazer isso: Extraia o preço médio da categoria que nos interessa (aquela a que pertence uma linha com o valor ausente, ou seja, 'hair care'). Para fazer isso, faça a indexação de um objeto Series usando um número de índice e salve na variável mean_val. Observação: se você precisa encontrar o índice necessário, procure-o no resultado da tarefa anterior.
Imprima mean_val.
mean_val = avg_per_category[2]
print(mean_val)

# Agora é hora de substituir o valor ausente por uma média na sua categoria. Em Python, você pode usar o atributo loc[] para fazer isso. Comece localizando a linha que contém o valor que você quer substituir:
    category      product  price
7  hair care  conditioner    NaN

#  Em seguida, passe o índice apropriado e o nome da coluna para loc[] e use o caractere = para definir o valor desejado. Você pode determinar o índice e o nome da coluna a serem usados em loc[] examinando as linhas que contêm o valor ausente. Quando terminar, imprima a variável df.
df.loc[7, 'price'] = mean_val
print(df)

5ª - Duplicados
# o nosso conjunto de dados tem problemas, incluindo duplicados. Para identificar os duplicados, aplicamos a função value_counts() à coluna 'product':
print(df['product'].value_counts())
product
lipstic        1
LIPSTIC        1
pacifier       1
shampoo        1
diapers        1
lotion         1
hair gel       1
conditioner    1
Name: count, dtype: int64

# percebemos que 'lipstic' e 'LIPSTIC' aparecem na coluna como valores separados. Para lidar com isso, recomendamos criar uma nova coluna em que todos os valores estejam em minúsculas, para garantir a consistência. Substitua a coluna 'product' por uma versão em letras minúsculas e imprima novamente.
df['product'] = df['product'].str.lower()
print(df['product'])

0        lipstic
1        lipstic
2       pacifier
3        shampoo
4        diapers
5         lotion
6       hair gel
7    conditioner
Name: product, dtype: object

# Por fim, vamos lidar com os duplicados. Depois de converter os valores da coluna 'product' para minúsculas, o conjunto de dados está assim:
+---+------------+-------------+-------+
|   | category   | product     | price |
+---+------------+-------------+-------+
| 0 | cosmetics  | lipstick    | 25.0  |
| 1 | cosmetics  | LIPSTIC     | 25.0  |
| 2 | tbc        | pacifier    | 9.0   |
| 3 | hair care  | shampoo     | 12.0  |
| 4 | baby care  | diapers     | 34.0  |
| 5 | cosmetics  | lotion      | 18.0  |
| 6 | hair care  | hair gel    | 21.0  |
| 7 | hair care  | conditioner | 16.5  |
+---+------------+-------------+-------+

# As linhas com os índices 0 e 1 são duplicados óbvios. Vamos descartá-las. Não se esqueça de redefinir os índices depois de descartar as linhas. Assim que terminar, imprima o DataFrame inteiro.
df = df.drop_duplicates(subset='product').reset_index(drop=True)
print(df)


PERGUNTA:
Vamos praticar como trabalhar com duplicados mais um pouco usando outro exemplo. Agora você está analisando dados sobre as vendas de carros Bentley para clientes diferentes e quer categorizá-los por cidade. O value_counts() na coluna de city retorna o seguinte:
New Your    1034
London      543
Paris       345
LONDON      32
 London     1
 Como você trata os valores de city?
 Reposta: Removo o espaço de London (com um espaço na frente) e converto todos os "Londons" para que a primeira letra fique maiúscula.

# Por fim, observamos anteriormente que há um valor 'tbc' na coluna 'category'. Confira como é esta linha:
    category    product     price
1       tbc    pacifier     9.0

# Vamos usar o método replace() para definir um valor apropriado aqui. Está claro que o produto 'pacifier' (chupeta) pertence à categoria 'baby care' (produtos para bebês) que temos no conjunto de dados. Depois de substituir o valor, imprima o DataFrame. use também o método str()
df['category'] = df['category'].str.replace('tbc', 'baby care')
print(df)

'''

'''
Capítulo 4 
Como especialista de dados, você vai trabalhar com grandes conjuntos: às vezes, eles terão milhões ou até bilhões de linhas. No entanto, geralmente será necessário trabalhar apenas com uma pequena porção do conjunto de dados completo.

Para encontrar as informações relevantes, você terá que selecionar os critérios apropriados para filtrar o conjunto. Depois, você poderá processar e analisar esses subconjuntos menores para explorar as questões de interesse de sua pesquisa.

Neste capítulo, vamos usar conjuntos de dados reais para te ensinar habilidades de filtragem mais avançadas. Ao final deste capítulo, você vai:

entender como índices funcionam em DataFrames e objetos Series;
aprender a indexar DataFrames usando loc[] e iloc[];
ser capaz de filtrar DataFrames escrevendo strings de consulta com o método query() e com base em condições lógicas complexas;
ser capaz de filtrar e substituir valores ao mesmo tempo usando o método where().
Serão necessárias cerca de 2 horas para concluir este capítulo. Você está com tudo pronto para se tornar um mestre da filtragem? Vamos lá!

4.1 - Índices em DataFrames e Series
# criar um objeto Series para demonstrar:
oceans = pd.Series(['Pacific', 'Atlantic', 'Indian', 'Southern', 'Arctic'])
print(oceans)

0     Pacific
1    Atlantic
2      Indian
3    Southern
4      Arctic
dtype: object


import pandas as pd

oceans = pd.Series(['Pacific', 'Atlantic', 'Indian', 'Southern', 'Arctic'])

print(oceans.index)
RangeIndex(start=0, stop=5, step=1) 

print(type(oceans.index)) # quando o index é o padrão do pandas a saida é assim tipo Rangeindex, se o index for definido pelo usuário a saída é diferente, como veremos mais adiante.
<class 'pandas.core.indexes.range.RangeIndex'>


Explicação do RangeIndex:
O tipo RangeIndex tem três parâmetros: start=, stop= e step=.

start= é o primeiro índice de um objeto Series ou um DataFrame.
stop= é o último índice. Como você pode ver, ele não está incluído em um objeto Series ou DataFrame.
step= é o passo dado ao mover do primeiro índice ao último. Por padrão, é 1.

# vamos definir os valores de índice usando uma lista de números inteiros de 1 a 5. Para isso, atribuímos a nossa lista de números ao atributo index de oceans:
oceans.index = [1, 2, 3, 4, 5]

print(oceans.index)
Int64Index([1, 2, 3, 4, 5], dtype='int64')

print(type(oceans.index))
<class 'pandas.core.indexes.numeric.Int64Index'>

# também podemos 
oceans = pd.Series(['Pacific', 'Atlantic', 'Indian', 'Southern', 'Arctic'],
                   index=[1, 2, 3, 4, 5])

print(oceans.index)
print(type(oceans.index))

'''