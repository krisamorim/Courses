import pandas as pd
cholera = pd.read_csv('/datasets/cholera.csv')
print(cholera)

'''
region	Property	country	total_cases	imported_cases	deaths	case_fatality_rate	notes
Asia	0	Afghanistan	33	0	1	3	NaN
Asia	1	India	385	NaN	3	0.7	NaN
Asia	2	Iran	634	625	4	0.6	NaN
Asia	3	Yemen	1032481	0	2261	0.2	NaN
Asia	4	China	14	NaN	0	0	NaN
Asia	5	Qatar	5	5	0	0	NaN
Asia	6	Malaysia	2	0	0	0	NaN
Asia	7	Nepal	7	NaN	0	0	NaN
Asia	8	UAE	12	12	0	0	NaN
Asia	9	Saudi Arabia	5	5	0	0	NaN
Asia	10	Singapore	3	3	0	0	NaN
Asia	11	Thailand	8	0	0	0	NaN
Asia	12	Philippines	134	NaN	2	1.5	NaN
Asia	13	South Korea	5	5	0	0	NaN
Asia	14	Japan	7	5	0	0	NaN
Americas	15	Haiti	13681	0	159	1.2	NaN
Americas	16	Dominican Republic	122	0	4	3.3	NaN
Americas	17	Canada	4	3	0	0	NaN
Americas	18	USA	11	9	0	0	NaN
Africa	19	All countries	179835	NaN	3220	1.8	no information on imported cases
Europe	20	All countries	NaN	NaN			no reports in 2017
Oceania	21	Australia	3	3	0	0	NaN
World	22	All countries	1227391	675	5654	0.5	NaN


Recebemos uma descrição das colunas do conjunto de dados. Isso é o que ele nos diz:

'region' e 'country' indicam a localização geográfica
'total_cases' número total de casos de cólera
'imported_cases' quantos casos foram importados de outros países
'deaths' - o número de casos letais
'case_fatality_rate' - armazena a taxa de mortalidade
'notes' contém strings com certos comentários

 Normalmente usamos o método isna() com o método sum(). A função sum() conta todos os valores True e retorna sua soma:
'''

print(cholera.isna().sum()) #or cholera.isnull().sum()

'''
column	0
country	0
total_cases	1
imported_cases	6
deaths	1
case_fatality_rate	1
notes	21
dtype: int64	0

Substituição de valores
Para preservar todas as linhas com dados valiosos, substituiremos os valores NaN na coluna 'imported_cases' por zeros.

Podemos fazer isso usando o método fillna(), que retorna uma cópia da coluna original com todos os valores NaN substituídos pelo valor especificado.
'''
cholera['imported_cases'] = cholera['imported_cases'].fillna(0) #or just cholera['imported_cases'].fillna(0, inplace=True)
print(cholera)

'''
Resultado:

region	index	country	total_cases	imported_cases	deaths	case_fatality_rate	notes
Asia	0	Afghanistan	33	0	1	3	NaN
Asia	1	India	385	0	3	0.7	NaN
Asia	2	Iran	634	625	4	0.6	NaN
Asia	3	Yemen	1032481	0	2261	0.2	NaN
Asia	4	China	14	0	0	0	NaN
Asia	5	Qatar	5	5	0	0	NaN
Asia	6	Malaysia	2.0	0	0	0	NaN
Asia	7	Nepal	7	0	0	0	NaN
Asia	8	UAE	12	12	0	0	NaN
Asia	9	Saudi Arabia	5	5	0	0	NaN
Asia	10	Singapore	3	3	0	0	NaN
Asia	11	Thailand	8	0	0	0	NaN
Asia	12	Philippines	134	0	2	1.5	NaN
Asia	13	South Korea	5	5	0	0	NaN
Asia	14	Japan	7	5	0	0	NaN
Americas	15	Haiti	13681	0	159	1.2	NaN
Americas	16	Dominican Republic	122	0	4	3.3	NaN
Americas	17	Canada	4	3	0	0	NaN
Americas	18	USA	11	9	0	0	NaN
Africa	19	All countries	179835	0	3220	1.8	no information on imported cases
Europe	20	All countries	NaN	0			no reports in 2017
Oceania	21	Australia	3	3	0	0	NaN
World	22	All countries	1227391	675	5654

A propósito, você pode até usar o ciclo for para substituir os valores ausentes. Tudo o que você precisa é criar uma lista que vai conter todas as colunas nas quais você deseja fazer a substituição e, em seguida, iterar sobre esses nomes para fazer a substituição:

'''

# percorrendo os nomes das colunas e substituindo valores ausentes com 0s
columns_to_replace = ['imported_cases']

for col in columns_to_replace:
    cholera[col].fillna(0, inplace=True)


'''
Tarefa 1
Escreva um código que some o número de valores ausentes em todas as colunas do conjunto de dados. Armazene o resultado na variável mis_val e imprima-o.

import pandas as pd
df = pd.read_csv('/datasets/music_log_raw.csv')
mis_val = df.isna().sum()
print(mis_val)

'''

'''
Remoção de linhas
Para remover linhas com valores ausentes em um DataFrame pandas, use o método dropna(). Esse método remove linhas com pelo menos um valor ausente. Você também pode especificar uma lista de colunas para o parâmetro subset= e ele vai remover as linhas com valores nulos apenas nessas colunas.

cholera = cholera.dropna(subset=['total_cases', 'deaths', 'case_fatality_rate'])
print(cholera)

region	index	country	total_cases	imported_cases	deaths	case_fatality_rate	notes
Asia	0	Afghanistan	33	0	1	3	NaN
Asia	1	India	385	0	3	0.7	NaN
Asia	2	Iran	634	625	4	0.6	NaN
Asia	3	Yemen	1032481	0	2261	0.2	NaN
Asia	4	China	14	0	0	0	NaN
Asia	5	Qatar	5	5	0	0	NaN
Asia	6	Malaysia	2	0	0	0	NaN
Asia	7	Nepal	7	0	0	0	NaN
Asia	8	UAE	12	12	0	0	NaN
Asia	9	Saudi Arabia	5	5	0	0	NaN
Asia	10	Singapore	3	3	0	0	NaN
Asia	11	Thailand	8	0	0	0	NaN
Asia	12	Philippines	134	0	2	1.5	NaN
Asia	13	South Korea	5	5	0	0	NaN
Asia	14	Japan	7	5	0	0	NaN
Americas	15	Haiti	13681	0	159	1.2	NaN
Americas	16	Dominican Republic	122	0	4	3.3	NaN
Americas	17	Canada	4	3	0	0	NaN
Americas	18	USA	11	9	0	0	NaN
Africa	19	All countries	179835	0	3220	1.8	no information on imported cases
Oceania	21	Australia	3	3	0	0	NaN
World	22	All countries	1227391	675	5654	0.5	NaN

'''

'''
Agora, removeremos toda a coluna 'notes', que consiste quase inteiramente em valores ausentes. Esse comando irá remover todas as colunas que tenham valores ausentes. Como 'notes' é a única coluna com valores ausentes, podemos usar essa opção com segurança para removê-la.

cholera = cholera.dropna(axis='columns')
print(cholera)

Esteja ciente de que se você tiver várias colunas com valores ausentes, cholera.dropna(axis='columns') eliminará todas elas. Isso normalmente não é o que queremos. Em vez disso, você pode usar o método drop() para controlar quais colunas deseja descartar. Isso é o que você deve fazer se quiser descartar apenas a coluna 'notes' usando o método drop():

cholera = cholera.drop(labels=['notes'], axis='columns')


Ambos drop() e dropna() suportam o argumento inplace=, que permite realizar a operação no local sem reatribuição. Aqui está um exemplo de como usar drop() para realizar uma substituição sem reatribuição:

cholera.drop(labels=['notes'], axis='columns', inplace=True)

'''

'''
Escreva código para percorrer as colunas genre, Artist e track do DataFrame df e substitua todos os valores ausentes pela string 'no_info'. A lista de colunas a serem substituídas está armazenada na variável columns_to_replace.

Após realizar as substituições, verifique novamente o número de valores ausentes usando isna().sum()
'''
import pandas as pd

df = pd.read_csv('/datasets/music_log_raw.csv')

columns_to_replace = ['genre', 'Artist', 'track']

for col in columns_to_replace:
	# Escreva seu código aqui
	df[col].fillna('no_info', inplace=True)

print(df.isna().sum())


'''
Tarefa 3
Agora vamos remover NaNs na coluna total play substituindo-os por 0.

Após realizar as substituições, verifique novamente o número de valores ausentes usando isna().sum()
'''
import pandas as pd

df = pd.read_csv('/datasets/music_log_raw.csv')

# escreva seu código aqui
df['total play'].fillna(0, inplace=True)

print(df.isna().sum())
