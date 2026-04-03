'''Agora você sabe como importar pandas, criar DataFrames e verificar seus atributos dtypes, columns e shape diretamente ou usando o método info(): '''

import pandas as pd

# preparando os dados e os nomes das colunas
atlas = [
      ['France', 'Paris'],  
        ['Russia', 'Moscow'],  
        ['China', 'Beijing'],  
        ['Mexico', 'Mexico City'],  
        ['Egypt', 'Cairo'],
]
geography = ['country', 'capital']

# fazendo um DataFrame
world_map = pd.DataFrame(data=atlas , columns=geography)

print(world_map.dtypes) #imprimindo o atributo dtypes
print(world_map.columns) #imprimindo o atributo columns
print(world_map.shape) #imprimindo o atributo shape
print(world_map.info()) #imprimindo todos os atributos de uma só vez

'''Você também pode criar DataFrames a partir de listas e arquivos CSV e Excel e usar os métodos head() e tail():'''

df = pd.read_csv('/datasets/music_log_chpt_11.csv') # ler um arquivo CSV

print(df.head()) # imprimir as primeiras 5 linhas do DataFrame

df2 = pd.read_excel('/datasets/music_log.xlsx')# ler um arquivo Excel

print(df2.tail()) # imprimir as últimas 5 linhas do DataFrame

'''Você pode indexar seu DataFrame usando a notação completa e abreviada e também aplicar expressões lógicas e métodos count(), sum() e mean():'''

# encontrando a média usando a notação completa e a expressão ==
mean_duration = df[df.loc[:, 'genre'] == 'pop']['total play'].mean()
# encontrando o número de músicas usando a notação abreviada e a expressão <=
count_duration = df[df['total play'] <= 130]['total play'].count()
# encontrando a média usando a notação abreviada e a expressão ==
sum_duration = df[df['genre'] == 'pop']['total play'].sum()