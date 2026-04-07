from pathlib import Path
import pandas as pd

#get file path
caminho_arquivo = Path(__file__).resolve()
#create path to dataframe
dataframePath = caminho_arquivo.parent / "df.csv"
#read dataframe
df = pd.read_csv(dataframePath)
print(df.duplicated().sum())

'''
Tarefa 1
No trecho de código abaixo, você encontrará a variável pop, que armazena um DataFrame filtrado contendo apenas músicas pop. Seu objetivo é determinar o número de duplicados neste DataFrame e armazenar este valor na variável duplicates. E, finalmente, imprima esta variável.
'''

pop = df[df['genre'] == 'pop']

#amount of duplicates in pop dataframe
duplicates = pop.duplicated().sum()
# print(duplicates)

#remove duplicates from pop dataframe
df = df.drop_duplicates() #or df.drop_duplicates(inplace=True)
print(df.duplicated().sum())
'''tualizar os índices quando você remove linhas. Para fazer isso, chame o método reset_index(). Isso criará um novo DataFrame no qual:

Os índices do DataFrame original vão estar localizados em uma nova coluna chamada 'index'.
Novos índices serão definidos em ordem para todas as linhas no DataFrame.  Normalmente, queremos descartar essa coluna 'index'. Para fazer isso, basta definir o parâmetro drop= como True:'''

df = df.reset_index(drop=True)


print(df.head())


'''
Tarefa 2
Usando os dados da tarefa anterior, agora precisamos descartar as linhas duplicadas do DataFrame pop. O DataFrame resultante deve ser armazenado na mesma variável pop. Depois de limpar o DataFrame, verifique novamente o número de duplicados e imprima esse número.
'''

pop = pop.drop_duplicates()

print(pop.duplicated().sum())