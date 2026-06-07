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
#Int64Index([1, 2, 3, 4, 5], dtype='int64')
print(type(oceans.index))
#<class 'pandas.core.indexes.numeric.Int64Index'>

#vamos definir os valores de índice como strings e ver qual tipo de dados teremos no índice:
oceans = pd.Series(['Pacific', 'Atlantic', 'Indian', 'Southern', 'Arctic'],
                   index=['A', 'B', 'C', 'D', 'E'])

print(oceans)
print()
print(oceans.index)
print(type(oceans.index))

# A     Pacific
# B    Atlantic
# C      Indian
# D    Southern
# E      Arctic
# dtype: object

# Index(['A', 'B', 'C', 'D', 'E'], dtype='object')
# <class 'pandas.core.indexes.base.Index'>


#REVISÃO SOBRE loc[]

#criando um DataFrame:


import pandas as pd

states  = ['Alabama', 'Alaska', 'Arizona', 'Arkansas']
flowers = ['Camellia', 'Forget-me-not', 'Saguaro cactus blossom', 'Apple blossom']
insects = ['Monarch butterfly', 'Four-spotted skimmer dragonfly', 'Two-tailed swallowtail', 'European honey bee']
index   = ['state 1', 'state 2', 'state 3', 'state 4']

df = pd.DataFrame({'state': states, 'flower': flowers, 'insect': insects}, index=index)

print(df)
#          state              flower                   insect
# state 1   Alabama           Camellia                 Monarch butterfly
# state 2    Alaska           Forget-me-not            Four-spotted skimmer dragonfly
# state 3   Arizona           Saguaro cactus blossom   Two-tailed swallowtail
# state 4  Arkansas           Apple blossom            European honey bee

Podemos acessar elementos do DataFrame com loc[] passando valores de índice e nomes de colunas, como df.loc[index_value, col_name]. Assim, veja como podemos obter o inseto do estado de Arkansas:

print(df.loc['state 4', 'insect'])
#European honey bee

# Também podemos usar loc[] para obter vários elementos como um objeto Series ou outro DataFrame. Para obter vários elementos, tudo o que você precisa fazer é passar para loc[] uma lista de índices e uma lista de colunas da seguinte maneira: df.loc[[index_value_1, index_value_1], [col_name_1, col_name_2]]

filtered_df = df.loc[["state 1", "state 3"],['flower', 'insect']]
print(filtered_df)
#                         flower                  insect
#state 1                Camellia       Monarch butterfly
#state 3  Saguaro cactus blossom  Two-tailed swallowtail

usar indexação para obter um intervalo de índices para uma única coluna. Para fazer isso, precisamos apenas especificar o primeiro e o último índice separados por um caractere :. Aqui está um exemplo que retorna as flores dos três primeiros índices de um DataFrame:

print(df.loc['state 1': 'state 3', 'flower'])
# state 1                  Camellia
# state 2             Forget-me-not
# state 3    Saguaro cactus blossom
# Name: flower, dtype: object

#De forma parecida, você pode selecionar várias colunas, bem como vários índices:

print(df.loc['state 1': 'state 3', 'flower': 'insect'])
#                         flower                          insect
# state 1                Camellia               Monarch butterfly
# state 2           Forget-me-not  Four-spotted skimmer dragonfly
# state 3  Saguaro cactus blossom          Two-tailed swallowtail


#obter apenas a coluna 'insect de todos os estados, exceto Alabama. 
df.loc['state 2':, 'insect']

#tabela de comandos de sintaxe de loc[]:
#+-------------------------------------------+----------------------------------+
#| Tipo                                      | Exemplo                         |
#+-------------------------------------------+----------------------------------+
#| Uma célula                                | .loc['state 3', 'flower']       |
#| Uma coluna                                | .loc[:, 'state']                |
#| Múltiplas colunas                         | .loc[:, ['flower', 'insect']]   |
#| Múltiplas colunas consecutivas (fatia)    | .loc[:, 'state':'insect']       |
#| Uma linha                                 | .loc['state 1']                 |
#| Todas as linhas, começando                | .loc['state 2':]                |
#| com a linha especificada                  |                                  |
#| Todas as linhas, até a linha              | .loc[:'state 3']                |
#| especificada                              |                                  |
#| Múltiplas linhas consecutivas (fatia)     | .loc['state 2':'state 4']       |
#+-------------------------------------------+----------------------------------+


#Indexação usando iloc[]
#Enquanto loc[] usa rótulos de índices e colunas para acessar elementos, iloc[] usa números inteiros para designar as posições dos elementos que você deseja obter.
#Dataframe
#            state                  flower                          insect
#state 1   Alabama                Camellia               Monarch butterfly
#state 2    Alaska           Forget-me-not  Four-spotted skimmer dragonfly
#state 3   Arizona  Saguaro cactus blossom          Two-tailed swallowtail
#state 4  Arkansas           Apple blossom              European honey bee

print(df.iloc[3, 2])
#European honey bee

#no loc: df.loc[['state 1', 'state 3'], ['flower', 'insect']]
#no iloc: df.iloc[[0, 2], [1:]]
#                          flower                  insect
# state 1                Camellia       Monarch butterfly
# state 3  Saguaro cactus blossom  Two-tailed swallowtail

#A propósito, você também pode usar indexação negativa. Aqui está um exemplo que seleciona a última coluna (que tem o índice Python de -1) e a primeira e a terceira linhas (os índices Python 0 e 2):

print(df.iloc[[0, 2], -1])
#state 1         Monarch butterfly
#state 3    Two-tailed swallowtail
#Name: insect, dtype: object

#Alteração do índice de um DataFrame usando o método set_index()

df = df.set_index('state') # substitui o índice padrão por uma coluna do DataFrame, nesse caso a coluna 'state'
print(df)
#                           flower                          insect
# state                                                           
# Alabama                 Camellia               Monarch butterfly
# Alaska             Forget-me-not  Four-spotted skimmer dragonfly
# Arizona   Saguaro cactus blossom          Two-tailed swallowtail
# Arkansas           Apple blossom              European honey bee

print(df.index)
# Index(['Alabama', 'Alaska', 'Arizona', 'Arkansas'], dtype='object', name='state')

#O nome da coluna state será inserido como indice zero, para que isso não ocorra utilize o comando abaixo

df.index.name = None
print(df)
#                           flower                          insect
# Alabama                 Camellia               Monarch butterfly
# Alaska             Forget-me-not  Four-spotted skimmer dragonfly
# Arizona   Saguaro cactus blossom          Two-tailed swallowtail
# Arkansas           Apple blossom              European honey bee
print(df.index)
# Index(['Alabama', 'Alaska', 'Arizona', 'Arkansas'], dtype='object')


#Filtragem com strings de consulta e o método query()
No data frame df = pd.read_csv('/datasets/vg_sales.csv') temos a seguinte saida para df.head() e df.info():
+---------------------------+----------+-----------------+--------------+-----------+-----------+----------+----------+----------+--------------+------------+
| name                      | platform | year_of_release | genre        | publisher | developer | na_sales | eu_sales | jp_sales | critic_score | user_score |
+---------------------------+----------+-----------------+--------------+-----------+-----------+----------+----------+----------+--------------+------------+
| Wii Sports                | Wii      | 2006.0          | Sports       | Nintendo  | Nintendo  | 41.36    | 28.96    | 3.77     | 76.0         | 8.0        |
| Super Mario Bros.         | NES      | 1985.0          | Platform     | Nintendo  | NaN       | 29.08    | 3.58     | 6.81     | NaN          | NaN        |
| Mario Kart Wii            | Wii      | 2008.0          | Racing       | Nintendo  | Nintendo  | 15.68    | 12.76    | 3.79     | 82.0         | 8.3        |
| Wii Sports Resort         | Wii      | 2009.0          | Sports       | Nintendo  | Nintendo  | 15.61    | 10.93    | 3.28     | 80.0         | 8.0        |
| Pokemon Red/Pokemon Blue  | GB       | 1996.0          | Role-Playing | Nintendo  | NaN       | 11.27    | 8.89     | 10.22    | NaN          | NaN        |
+---------------------------+----------+-----------------+--------------+-----------+-----------+----------+----------+----------+--------------+------------+


DataFrame Info
==============

+-----------------+--------+------------+----------+
| Column          | NonNull| Dtype      | Missing  |
+-----------------+--------+------------+----------+
| name            | 16717  | object     | 0        |
| platform        | 16717  | object     | 0        |
| year_of_release | 16448  | float64    | 269      |
| genre           | 16717  | object     | 0        |
| publisher       | 16663  | object     | 54       |
| developer       | 10096  | object     | 6621     |
| na_sales        | 16717  | float64    | 0        |
| eu_sales        | 16717  | float64    | 0        |
| jp_sales        | 16717  | float64    | 0        |
| critic_score    | 8137   | float64    | 8580     |
| user_score      | 7590   | float64    | 9127     |
+-----------------+--------+------------+----------+

Total de registros: 16.717
Total de colunas:   11
Uso de memória:     ~1.4 MB

Há muitas colunas no conjunto de dados. Muitas delas são autoexplicativas, mas vamos detalhar algumas daquelas que talvez não sejam:

'platform': é o console para o qual o jogo foi lançado
'xx_sales': são as vendas para a América do Norte (NA), Europa (EU) e Japão (JP) em milhões de dólares
'critic_score': é a nota de 0 a 100 dada ao jogo pelos críticos
'user_score': é a nota de 0 a 100 dada ao jogo pelos consumidores


Vamos filtrar os dados de forma que apenas selecionemos os jogos cujas vendas no Japão foram de pelo menos um milhão de dólares:
mask = df['jp_sales'] >= 1
print(df[mask][['name', 'jp_sales']])

Temos a seguinte saída:
+------+----------------------------------------------+----------+
| idx  | name                                         | jp_sales |
+------+----------------------------------------------+----------+
| 0    | Wii Sports                                   | 3.77     |
| 1    | Super Mario Bros.                            | 6.81     |
| 2    | Mario Kart Wii                               | 3.79     |
| 3    | Wii Sports Resort                            | 3.28     |
| 4    | Pokemon Red/Pokemon Blue                     | 10.22    |
| ...  | ...                                          | ...      |
| 1970 | Tag Team Match M.U.S.C.L.E.                  | 1.05     |
| 1971 | Derby Stallion 96                            | 1.04     |
| 1972 | Adventure Island                             | 1.05     |
| 2051 | Oshare Majo Love and Berry: DS Collection    | 1.01     |
| 2065 | Jissen Pachi-Slot Hisshouhou: Hokuto no Ken  | 1.00     |
+------+----------------------------------------------+----------+

[243 rows x 2 columns]

No código acima, a variável mask contém um objeto Series com valores True e False. True indica que um valor na coluna 'jp_sales' tem vendas iguais ou maiores que um milhão de dólares, enquanto False indica vendas abaixo desse valor.
Em seguida, usamos essa máscara para filtrar o DataFrame original com df[mask] e selecionar duas colunas de interesse: ['name', 'jp_sales'].
Para simplificar, estamos visualizando apenas as colunas 'name' e 'jp_sales'. É claro, poderíamos ter feito isso sem criar a variável mask e simplesmente colocado a expressão de máscara na nossa linha de filtragem no código. Aqui está como isso seria:  print(df[df['jp_sales'] >= 1][['name', 'jp_sales']])

# filtragem usando o método query()
print(df.query("jp_sales > 1")[['name', 'jp_sales']])

Para filtrar usando query() com base nas comparações de strings, você precisa colocar a string entre aspas. Por exemplo, vamos selecionar apenas os jogos publicados pela Nintendo:
print(df.query("publisher == 'Nintendo'")[['name', 'publisher']])

#                        name publisher
# 0                Wii Sports  Nintendo
# 1         Super Mario Bros.  Nintendo
# 2            Mario Kart Wii  Nintendo
# 3         Wii Sports Resort  Nintendo
# 4  Pokemon Red/Pokemon Blue  Nintendo

#TAREFA 1
Agora use query() para filtrar os dados. Mantenha apenas as linhas em que as colunas 'publisher' e 'developer' têm os mesmos valores. Seu objetivo é verificar a igualdade entre as duas colunas. Para isso, selecione o operador lógico que faz isso.

A variável cols, que já está presente no pré-código, especifica as colunas que queremos selecionar do resultado da consulta. Para selecionar apenas as colunas de interesse, use a variável cols imediatamente após o método query(). Aqui está a sintaxe: df.query(...)[cols].

Por fim, atribua o resultado a uma variável chamada df_filtered e imprima as 5 primeiras linhas.

import pandas as pd

df = pd.read_csv('/datasets/vg_sales.csv')

cols = ['name', 'publisher', 'developer']

df_filtered = df.query("publisher == developer")[cols]
print(df_filtered.head())

# Filtragem usando o método isin()

import pandas as pd
df = pd.read_csv('/datasets/vg_sales.csv')
handhelds = ['3DS', 'DS', 'GB', 'GBA', 'PSP']
print(df[df['platform'].isin(handhelds)][['name', 'platform']])


#                                                     name platform
# 4                               Pokemon Red/Pokemon Blue       GB
# 5                                                 Tetris       GB
# 6                                  New Super Mario Bros.       DS
# 10                                            Nintendogs       DS
# 11                                         Mario Kart DS       DS
# ...                                                  ...      ...
# 16702                           Mezase!! Tsuri Master DS       DS
# 16703  Eiyuu Densetsu: Sora no Kiseki Material Collec...      PSP
# 16706                                           Plushees       DS
# 16710                 Woody Woodpecker in Crazy Castle 5      GBA
# 16715                                   Spirits & Spells      GBA

# [4801 rows x 2 columns]

df['platform'].isin(handhelds) verifica se os valores na coluna 'platform' são iguais a um dos valores da lista handhelds, que representa os consoles portáteis.
df[df['platform'].isin(handhelds)] filtra o DataFrame mantendo apenas as linhas retornadas como resultado da verificação da igualdade que executamos na etapa anterior.
Por fim, selecionamos apenas duas colunas do DataFrame filtrado: ['name', 'platform'] descartando o resto das colunas. Lembre-se de que usamos colchetes duplos para selecionar várias colunas, por isso o código acima tem [['name', 'platform']].
Poderíamos ter feito a mesma filtragem verificando se 'platform' era igual a '3DS' ou 'DS' ou 'GB', etc. Usar isin() é muito mais conveniente quando temos muitas condições para verificar. Imagine se quiséssemos verificar a existência em uma lista com dezenas ou centenas de valores!

podemos filtrar o DataFrame original extraindo apenas as linhas em que os valores na coluna 'platform' não estão na lista handhelds:

print(df[~df['platform'].isin(handhelds)][['name', 'platform']])

#comando anterior:
print(df[df['platform'].isin(handhelds)][['name', 'platform']])

#                                                                                                     name platform
# 0                                            Wii Sports      Wii
# 1                                     Super Mario Bros.      NES
# 2                                        Mario Kart Wii      Wii
# 3                                     Wii Sports Resort      Wii
# 7                                              Wii Play      Wii
# ...                                                 ...      ...
# 16711  SCORE International Baja 1000: The Official Game      PS2
# 16712                     Samurai Warriors: Sanada Maru      PS3
# 16713                                  LMA Manager 2007     X360
# 16714                           Haitaka no Psychedelica      PSV
# 16716                               Winning Post 8 2016      PSV

# [11916 rows x 2 columns]


#Filtragem usando a query
Também podemos verificar a existência de algo usando o método query() com a palavra-chave in na string de consulta.

Vamos ver como isso funciona em uma filtragem igual à anterior:
print(df.query("platform in @handhelds")[['name', 'platform']])

#sem query:
#print(df[df['platform'].isin(handhelds)][['name', 'platform']])

Como alternativa, você pode encontrar as linhas que não estão na lista usando a palavra-chave not in:

print(df.query("platform not in @handhelds")[['name', 'platform']])

Como a variável handhelds é externa ao DataFrame, temos que iniciá-la com o símbolo @ na string de consulta. Caso contrário, a pandas vai tentar encontrar uma coluna chamada 'handhelds' e vai exibir um erro quando não conseguir encontrá-la.

Tarefa 1
Imprima uma lista de todos os gêneros únicos no conjunto de dados chamando o método unique() na coluna 'genre'.

import pandas as pd

df = pd.read_csv('/datasets/vg_sales.csv')

unique_genres = df['genre'].unique()
print(unique_genres)
#['Sports' 'Platform' 'Racing' 'Role-Playing' 'Puzzle' 'Misc' 'Shooter'
 'Simulation' 'Action' 'Fighting' 'Adventure' 'Strategy']

 Tarefa 2
No pré-código, você tem duas variáveis:

cols, que contém as colunas de interesse: 'name' e 'genre'.
s_genres, que é uma lista de gêneros começando com a letra "S".
Seu objetivo é usar o método isin() com a lista dada s_genres para filtrar o DataFrame df de maneira a manter apenas as linhas onde o gênero de jogo não comece com a letra "S".

Depois de filtrar o DataFrame, use a variável cols para selecionar apenas as colunas 'name' e 'genre' e atribuir o resultado a uma variável chamada df_filtered. Por fim, imprima.

import pandas as pd

df = pd.read_csv('/datasets/vg_sales.csv')

cols = ['name', 'genre']
s_genres = ['Shooter', 'Simulation', 'Sports', 'Strategy']

df_filtered = df[~df['genre'].isin(s_genres)][cols]
print(df_filtered)

#                                                    name         genre
# 1                                     Super Mario Bros.      Platform
# 2                                        Mario Kart Wii        Racing
# 4                              Pokemon Red/Pokemon Blue  Role-Playing
# 5                                                Tetris        Puzzle
# 6                                 New Super Mario Bros.      Platform
# ...                                                 ...           ...
# 16710                Woody Woodpecker in Crazy Castle 5      Platform
# 16711  SCORE International Baja 1000: The Official Game        Racing
# 16712                     Samurai Warriors: Sanada Maru        Action
# 16714                           Haitaka no Psychedelica     Adventure
# 16715                                  Spirits & Spells      Platform

# [11489 rows x 2 columns]

Tarefa 3
Filtre todos os gêneros que não começam com "S" novamente, mas desta vez faça isso usando o método query(). Você vai precisar usar a palavra-chave not in na string de consulta para fazer isso. Use cols para selecionar apenas as colunas 'name' e 'genre' e atribua o resultado a uma variável chamada df_filtered. Por fim, imprima.

import pandas as pd

df = pd.read_csv('/datasets/vg_sales.csv')

cols = ['name', 'genre']
s_genres = ['Shooter', 'Simulation', 'Sports', 'Strategy']

# escreva seu código aqui
df_filtered = df.query("genre not in @s_genres")[cols]

print(df_filtered)

#                                                    name         genre
# 1                                     Super Mario Bros.      Platform
# 2                                        Mario Kart Wii        Racing
# 4                              Pokemon Red/Pokemon Blue  Role-Playing
# 5                                                Tetris        Puzzle
# 6                                 New Super Mario Bros.      Platform
# ...                                                 ...           ...
# 16710                Woody Woodpecker in Crazy Castle 5      Platform
# 16711  SCORE International Baja 1000: The Official Game        Racing
# 16712                     Samurai Warriors: Sanada Maru        Action
# 16714                           Haitaka no Psychedelica     Adventure
# 16715                                  Spirits & Spells      Platform

# [11489 rows x 2 columns]

#Uso de estruturas de dados externas para filtrar DataFrames
Para ilustrar o papel de índices na filtragem, vamos criar nossos próprios DataFrames neste capítulo. Vamos revisar brevemente como usar uma lista externa para filtrar o nosso DataFrame com query(). Para descobrir se os valores da coluna 'a' estão na lista our_list, vamos escrever a consulta "a in @our_list" (a em @our_list).

import pandas as pd

our_list = [2, 5, 10]
df = pd.DataFrame(
    {
        'a': [2, 3, 10, 11, 12],
        'b': [5, 4, 3, 2, 1],
        'c': ['X', 'Y', 'Y', 'Y', 'Z'],
    }
)
print(df)
print()
print(our_list)
print()
print(df.query("a in @our_list"))

#     a  b  c
# 0   2  5  X
# 1   3  4  Y
# 2  10  3  Y
# 3  11  2  Y
# 4  12  1  Z

# [2, 5, 10]

#     a  b  c
# 0   2  5  X
# 2  10  3  Y
'''
