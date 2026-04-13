import pandas as pd

# as distâncias são armazenadas em uma lista de listas
measurements = [
    ['Sun', 146, 152],
    ['Moon', 0.36, 0.41], 
    ['Mercury', 82, 217], 
    ['Venus', 38, 261],
    ['Mars', 56, 401],
    ['Jupiter', 588, 968],
    ['Saturn', 1195, 1660],
    ['Uranus', 2750, 3150],
    ['Neptune', 4300, 4700],
    ['Halley\'s comet', 6, 5400]
    ]

# os nomes das colunas são armazenados na variável de cabeçalho
header = ['Celestial bodies ','MIN', 'MAX'] 

# armazenando o DataFrame na variável celestial
celestial = pd.DataFrame(data=measurements, columns=header)

print(celestial.columns)# Index(['Celestial bodies ','MIN', 'MAX'], dtype='object')

#renaming
# Declarando um dicionário com os nomes antigos das colunas como as chaves
# e os novos nomes de colunas como os valores
columns_new ={
    "Celestial bodies ": "celestial_bodies",
    "MIN": "min_distance",
    "MAX": "max_distance",
    }

# Chamando o método rename e passando
#better way
celestial.rename(columns = columns_new, inplace = True)

#other way
# o dicionário como um argumento para o parâmetro columns
#celestial = celestial.rename(columns = columns_new)
print(celestial.columns)  #Index(['celestial_bodies', 'min_distance', 'max_distance'], dtype='object')



''' Tarefa 1
Agora é sua vez de praticar!

Primeiro, você precisa saber se algo está errado com os nomes das colunas e o que exatamente está errado. Então comece imprimindo os nomes das colunas da tabela df.'''

# print(df.columns)

df = pd.read_csv('/datasets/music_log_raw.csv')

columns_new = {
    '  user_id':'user_id',
    'total play':'total_play',
    'Artist':'artist',    
}

df.rename(columns = columns_new, inplace = True)

print(df.columns)



'''
Tarefa 3
Agora queremos que você faça a mesma renomeação, mas usando 3 métodos de string: strip(), lower() e replace(). Coloque os novos nomes das colunas na lista new_col_names.

Em seguida, imprima o atributo columns de df para confirmar que as alterações foram aplicadas.
'''

new_col_names = []

for old_name in df.columns:
    name_stripped = old_name.strip()
    name_lowered = name_stripped.lower()
    name_no_spaces = name_lowered.replace(' ','_')
    new_col_names.append(name_no_spaces)
df.columns = new_col_names

print(df.columns)




