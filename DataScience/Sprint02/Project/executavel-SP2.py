import pandas as pd
import os

#comando para limpar o terminal
os.system('cls' if os.name == 'nt' else 'clear')

current_path = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_path, 'music_project_en.csv')
df = pd.read_csv(file_path)

#ver numero de linhas e colunas
# print(df.shape)

# verificar o tipo de dados de cada coluna, qunatidade de linahs e colunas
# print(df.info())

# ver as 3 primeira linhas do dataframe
# print(df.head(3)

#código para obter o nome das colunas
# print(f'Columns before rename: {df.columns}')

#renaming columns using a dictionary
new_col_names = []

for old_name in df.columns:
    name_stripped = old_name.strip()
    name_lowered = name_stripped.lower()
    name_no_spaces = name_lowered.replace(' ','_')
    new_col_names.append(name_no_spaces)
df.columns = new_col_names

#Precisamos aplicar a regra de sublinhado no lugar de espaço à coluna userid. Deveria ser user_id. Renomeie essa coluna e imprima os nomes de todas as colunas quando terminar.
df.rename(columns={'userid': 'user_id'}, inplace=True)

# print(f'Columns after rename: {df.columns}')

# mostrar o total de valores nulos nas colunas
# print(df.isna().sum())

#mostrar o total de valores nulos nas colunas em porcentagem somente com duas casa decimais
# print(f'Percentage of null values in each column (before remove nulls):\n{df.isna().mean().round(2) * 100}')

#mostrar as 10 primeiras linhas que tem track nulo
# print(df[df['track'].isna()].head(10))

# remover as linhas que tem track nulo, artist nulo ou genre nulo
# df.dropna(subset=['track', 'artist', 'genre'], inplace=True)
# print(df.shape)

#criar uma lista para armazenar os nomes das colunas nas quais precisamos fazer a substituição. Depois criar um for para percorra as colunas nas quais a substituição seja necessária e faça a substituição.
columnsWithNull = ['track', 'artist', 'genre']
for column in columnsWithNull:
    df[column].fillna('Unknown', inplace=True)

#mostrar o total de valores nulos nas colunas em porcentagem somente com duas casa decimais
# print(f'Percentage of null values in each column (after remove nulls):\n{df.isna().mean().round(2) * 100}')
# the command below shows the number of duplicated rows in the dataframe
# print(df.duplicated().sum())

# the command below shows the rows that are duplicated in the dataframe
# print(df[df.duplicated()])

# the command below shows all rows that user E7F07B46 duplicated in the dataframe
# print(df[df['userid'] == 'E7F07B46'])

#the command belows shows all rows wherer id is E7F07B46
# print(df[df['userid'] == 'E7F07B46'])

# a linha aseguir mostra em porcentagem a quantidade de duplicidade no arquivo
# print(df.shape)
# print(f'Percentage of duplicated rows in the dataframe: {df.duplicated().mean().round(2) * 100}')

#a linha a seguir mostr somente o numero total de duplicidades 
# print(f'Total number of duplicated rows in the dataframe: {df.duplicated().sum()}')

#remover duplicaos
df.drop_duplicates(inplace=True)

# print(df['genre'].unique())

#armazenar todos os valores unicos da coluna artist em uma variável chamada artists e imprima essa variável
artist = df['artist'].unique()
list_artist = []
for a in artist:
    list_artist.append(a)
# print(list_artist)

#salvar a lista em um arquivo txt chamao a.txt no caminho file_path
# with open(os.path.join(current_path, 'a.txt'), 'w') as f:
#     for item in list_artist:
#         f.write("%s\n" % item)

#salvar a lista em formato de lista mesmo em um arquivo txt chamao a.txt no caminho file_path
# with open(os.path.join(current_path, 'a.txt'), 'w') as f:
    # f.write(str(list_artist))

#salvar a saida do comando print(list_artist) em um arquivo txt chamado list_artist.txt no caminho file_path
# with open(os.path.join(current_path, 'list_artist.txt'), 'w', encoding='utf-8') as f:
    # f.write(str(list_artist))

#mostrar colunas do arquivo
# print(df.columns)

#busca na variavel list_artist o nome 'Vol.2' e retorna a posição
# print(list_artist.index('Elsie Morison/Alexander Young/Michael Langdon/Beecham Choral Society/Royal Philharmonic Orchestra/Sir Thomas Beecham'))

#verificar quantas vezes a aparece e a string 'Elsie Morison/Alexander Young/Michael Langdon/Beecham Choral Society/Royal Philharmonic Orchestra/Sir Thomas Beecham'
# print(df['artist'].str.contains('Elsie Morison/Alexander Young/Michael Langdon/Beecham Choral Society/Royal Philharmonic Orchestra/Sir Thomas Beecham', case=False, na=False).sum())

# print(df['artist'].str.contains('Richard Lewis/James Milligan/John Cameron/Owen Brannigan/Glyndebourne Chorus/Peter Gellhorn/Pro Arte Orchestra/Sir Malcolm Sargent', case=False, na=False).sum())

lista_artistas = [
    'Pink Floyd Floydhead',
    'FOrΣvΣrT',
    'Vol.2',
    'Christmas Hits',
    'Summer Hit Superstars',
    'Films Movie',
    'Mindfulness Meditation Music Spa Maestro',
    'Richard Lewis/James Milligan/John Cameron/Owen Brannigan/Glyndebourne Chorus/Peter Gellhorn/Pro Arte Orchestra/Sir Malcolm Sargent',
    '80s Greatest Hits',
    'Lo Mejor Del Rock De Los 80',
    'Elsie Morison/Alexander Young/Michael Langdon/Beecham Choral Society/Royal Philharmonic Orchestra/Sir Thomas Beecham',
    'Le\xadæther Strip'
]

#o código a seguire verifica quantas vezes cada item da lista lista_artistas aparece no dataframe, depois gera uma objeto com cada item seguido da quantidade de vezes que ele aparece e depois imprime a soma total de vezes que os itens da lista aparecem no dataframe
# total_count = 0
# for artista in lista_artistas:
#     count = df['artist'].str.contains(artista, case=False, na=False).sum()
    # total_count += count
    # print(f'{artista}: {count}')
# print(f'Total count of artists in the list: {total_count}')

#agora iremos remover todas as linhas do dataframe em que o nome do artista seja igual a algum item da lista lista_artistas
# print(df.shape)
for artista in lista_artistas:
    df = df[~df['artist'].str.contains(artista, case=False, na=False)]
# print(df.shape)


#ANALISANDO COLUNA GENRE
#armazenar todos os valores unicos da coluna genre em uma variável chamada genres e informar o total de valore sunicos da coluna genre
genres = df['genre'].unique()
list_genre = []
for a in genres:
    list_genre.append(a)

print(f'Total unique genres: {len(genres)}')


#agora verificar quantas vezes cada item da lista list_genre aparece no dataframe, depois gerar uma objeto com cada item seguido da quantidade de vezes que ele aparece e depois imprimir a soma total de vezes que os itens da lista aparecem no dataframe e criar um objeto do tipo dicionário onde a chave seja o nome do gênero e o valor seja a quantidade de vezes que ele aparece no dataframe em decrescente (ou seja, quem aparece mais vezes deve ser o primeiro item do dicionário)
total_count = 0
genre_count = {}
for genre in list_genre:
    count = df['genre'].str.contains(genre, case=False, na=False).sum()
    total_count += count
    genre_count[genre] = count
sorted_genre_count = dict(sorted(genre_count.items(), key=lambda item: item[1], reverse=True))
# print(f'Total count of genres in the list: {total_count}')

#remover da vairavel sorted_genre_count todas as palavras 'np.int64(' e ')' que aparecem no valor de cada item do dicionário
for key in sorted_genre_count:
    sorted_genre_count[key] = str(sorted_genre_count[key]).replace('np.int64(', '').replace(')', '')
print(sorted_genre_count)


#mostrar quantos valores duplicados tem na coluna genre
# print(df['genre'].duplicated().sum())


#salvar a saida do comando print(list_genero) em um arquivo txt chamado list_genero.txt no caminho file_path
# with open(os.path.join(current_path, 'list_genero.txt'), 'w', encoding='utf-8') as f:
    # f.write(str(list_genre))

#verificar quantas vezes aparece o termo 'hip-hop' na coluna genre no datafram df e depois verificar quantas vezes aparece o termo 'hip' e depois verificar quantas vezes aparece o termo 'hop'
# print(df['genre'].str.contains('hip-hop', case=False, na=False).sum())
# print(df['genre'].str.contains('hip', case=False, na=False).sum())
# print(df['genre'].str.contains('hop', case=False, na=False).sum())

'''
função replace_wrong_genres() com dois parâmetros:
wrong_genres= — essa é uma lista que contém todos os valores que você precisa substituir
correct_genre= — essa é uma string que você vai usar para a substituição
a função deve corrigir os nomes na coluna 'genre' da tabela df, isto é, substituindo cada valor da lista wrong_genres por valores de correct_genre
'''
def replace_wrong_genres(wrong_genres, correct_genre):
    for wrong_genre in wrong_genres:
        df['genre'] = df['genre'].str.replace(wrong_genre, correct_genre, case=False, regex=False)