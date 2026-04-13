import pandas as pd
import os

#comando para limpar o terminal
os.system('cls' if os.name == 'nt' else 'clear')

current_path = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_path, 'music_project_en.csv')
df = pd.read_csv(file_path)

#renomando as colunas do dataframe para lowercase, sem espaços e sem caracteres especiais
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

# percorrendo os cabeçalhos e substituindo valores ausentes por 'unknown'
columnsWithNull = ['track', 'artist', 'genre']
for column in columnsWithNull:
    df[column] = df[column].fillna('Unknown')

# contando duplicados explícitos
# print(df.duplicated().sum())

# removendo duplicados explícitos
df.drop_duplicates(inplace=True)

# visualizando nomes de gêneros únicos
# print(df['genre'].unique())

#gerar variável valores unicos de genre
# genre_unique = df['genre'].unique()
# print(genre_unique)
#preparando séries panda para localiza palavras com 'hi' no nome do gênero
# hi_genres_series = pd.Series(genre_unique)
#gerar variavel somente com itens de genre que tem 'hi' no nome
# result = hi_genres_series[hi_genres_series.str.contains('hi', case=False, na=False)]
#imprimir resultado como lista
# print(result.tolist())

#criando função para substituir gêneros errados por um gênero correto
def replace_wrong_genres(wrong_genres, correct_genre):
    # Usamos o método .replace do pandas
    # Ele aceita uma lista de valores para procurar e um valor único para substituir
    df['genre'] = df['genre'].replace(wrong_genres, correct_genre)
# Agora definimos os dados para a substituição
duplicados_hiphop = ['hip', 'hop', 'hip-hop'] # lista de erros
nome_correto = 'hiphop'                       # valor correto
# Chamamos a função
replace_wrong_genres(duplicados_hiphop, nome_correto)

# Agrupando pela coluna 'city' e contando os valores
# print(df.groupby('city')['user_id'].count())

#Função que filtre o DataFrame e retorne o total de músicas ouvidas para uma cidade e dia específico

df_by_city = df.groupby(by='city')['city'].count()
# print(df_by_city)


# Calculando as músicas escutadas em cada um desses três dias
df_by_day = df.groupby(by='day')['track'].count()
# print(df_by_day)








# #Primeiro, precisamos de uma função que filtre o DataFrame e retorne o total de entradas (músicas ouvidas) para uma combinação específica de cidade e dia.
# def number_tracks(day, city):
#     # Filtrando por dia e cidade
#     track_list = df[(df['day'] == day) & (df['city'] == city)]
    
#     # Contando a quantidde de usuários na lista resultante
#     track_list_count = track_list['user_id'].count()
    
#     return track_list_count

# #Agora, vamos chamar essa função seis vezes para obter os dados necessários de ambas as cidade
# # Resultados para Springfield
# spr_mon = number_tracks('Monday', 'Springfield')
# spr_wed = number_tracks('Wednesday', 'Springfield')
# spr_fri = number_tracks('Friday', 'Springfield')

# # Resultados para Shelbyville
# shel_mon = number_tracks('Monday', 'Shelbyville')
# shel_wed = number_tracks('Wednesday', 'Shelbyville')
# shel_fri = number_tracks('Friday', 'Shelbyville')

# #Para facilitar a visualização e a validação da hipótese, vamos organizar esses valores em um novo DataFrame.
# # Criando a tabela de resultados
# test_hypothesis_results = pd.DataFrame(
#     data=[
#         ['Springfield', spr_mon, spr_wed, spr_fri],
#         ['Shelbyville', shel_mon, shel_wed, shel_fri]
#     ],
#     columns=['city', 'monday', 'wednesday', 'friday']
# )

# print(test_hypothesis_results)