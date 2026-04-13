'''
Sprint 2 - Projeto

O trabalho de um analista é analisar dados para obter percepções valiosas dos dados e tomar decisões fundamentadas neles. Esse processo consiste em várias etapas: visão geral de dados, pré-processamento de dados e testes de hipóteses.

Hipóteses são suposições feitas sobre a população com base em uma amostra de dados. Essas suposições são testadas usando métodos estatísticos para determinar se elas são verdadeiras ou falsas. Testar uma hipótese envolve fazer uma declaração sobre a população, coletar dados e usar métodos estatísticos para testar essa declaração.

Sempre que fazemos análises, nós temos que formular hipóteses que depois poderemos testar. Às vezes nós aceitamos essas hipóteses; outras vezes, nós as rejeitamos. Para tomar as decisões certas, um negócio deve ser capaz de entender se está fazendo as suposições certas ou não.


Descrição do projeto
No contexto deste projeto, você vai testar uma hipótese relacionada às preferências musicais de duas cidades. Para isso, você vai analisar os dados de um serviço de streaming de música online para testar a hipótese apresentada abaixo e comparar o comportamento dos usuários nessas duas cidades.

Isso envolverá analisar os dados de um serviço de streaming real para comparar o comportamento dos usuários em Springfield e Shelbyville. O projeto é dividido em três etapas, cada uma das quais tem seus objetivos específicos.

Na Etapa 1, você fornecerá uma visão geral dos dados e escreverá suas observações. Na Etapa 2, você fará o pré-processamento dos dados, limpando-os. Finalmente, na Etapa 3, você testará a hipótese dando os passos de programação necessários para testar cada declaração e comentar seus resultados nos blocos apropriados.

Depois de concluir essas etapas, você será capaz de obter percepções valiosas dos dados e tomar decisões baseadas neles.

Hipótese
Para este projeto, reunimos os requisitos e preparamos uma hipótese que precisamos confirmar ou rejeitar.

Ao testar hipóteses, é importante perceber que elas podem ser totalmente aceitas, parcialmente aceitas, parcialmente rejeitadas ou totalmente rejeitadas.

Quando uma hipótese é totalmente aceita, isso significa que os resultados do teste confirmam a declaração feita sobre a população sem quaisquer dúvidas.

Se ela for parcialmente aceita, isso significa que os resultados confirmam a declaração até certo ponto, mas não suficientemente para aceitá-la totalmente.

Por outro lado, se uma hipótese for totalmente rejeitada, isso significa que os resultados do teste não confirmam a declaração feita sobre a população.

Finalmente, uma hipótese também pode ser parcialmente rejeitada se os dados indicarem que é falsa, mas você não puder rejeitá-la totalmente. Quando interpretamos os resultados de um teste de hipótese, é importante considerar todas essas diferentes possibilidades.

Aqui está a hipótese que precisamos aceitar ou rejeitar:

A atividade dos usuários é diferente dependendo do dia da semana e da cidade.


Instruções para completar o projeto
Preparamos para você um modelo de notebook, em que você pode escrever seu código e descrever suas análises. Para completar o projeto, preencha cada célula de código no modelo e edite as células Markdown nos casos em que o modelo solicitar que você explique seus resultados.

É uma boa prática sempre incluir uma introdução que descreve brevemente seus objetivos e uma conclusão que resume seus resultados na forma de células Markdown.

Antes de você começar, vamos revisar as três etapas do projeto novamente:

Etapa 1: visão geral dos dados. O notebook tem células prontas com instruções sobre que tipo de código escrever, bem como blocos de texto onde você pode escrever suas observações.

Etapa 2: pré-processamento de dados. Nesta etapa, você arrumará nomes de colunas e removerá valores ausentes e duplicados. Siga o esquema fornecido no notebook e certifique-se de escrever suas observações no final desta seção.

Etapa 3: teste da hipótese. Esta é a parte principal do seu projeto. Dê os passos de codificação necessários para testar cada declaração e comentar seus resultados nos blocos apropriados. Finalmente, resuma todo o projeto na seção "Conclusões".

No vídeo abaixo, abordamos alguns pontos essenciais nos quais você deve prestar atenção enquanto trabalha no seu projeto.

'''


'''
1. Introdução ¶
O trabalho de um analista é analisar dados para obter percepções valiosas dos dados e tomar decisões fundamentadas neles. Esse processo consiste em várias etapas, como visão geral dos dados, pré-processamento dos dados e testes de hipóteses.

Sempre que fazemos uma pesquisa, precisamos formular uma hipótese que depois poderemos testar. Às vezes nós aceitamos essas hipóteses; outras vezes, nós as rejeitamos. Para fazer as escolhas certas, um negócio deve ser capaz de entender se está fazendo as suposições certas ou não.

Neste projeto, você vai comparar as preferências musicais dos habitantes de Springfild e Shelbyville. Você vai estudar os dados de um serviço de streaming de música online para testar a hipótese apresentada abaixo e comparar o comportamento dos usuários dessas duas cidades.


1.1. Objetivo:
Teste a hipótese:

A atividade dos usuários é diferente dependendo do dia da semana e da cidade.

1.2. Etapas
Os dados sobre o comportamento do usuário são armazenados no arquivo /datasets/music_project_en.csv. Não há informações sobre a qualidade dos dados, então será necessário examiná-los antes de testar a hipótese.

Primeiro, você avaliará a qualidade dos dados e verá se seus problemas são significativos. Depois, durante o pré-processamento dos dados, você tentará tratar dos problemas mais críticos.

O seu projeto consistirá em três etapas:

Visão geral dos dados
Pré-processamento de dados
Teste da hipótese

2. Etapa 1. Visão geral dos dados

'''

import pandas as pd

df = pd.read_csv('/datasets/music_project_en.csv')
# Exiba as primeiras 10 linhas do DataFrame
print(df.head(10))
# obtendo informações gerais sobre os nossos dados
print(df.info())
'''
class 'pandas.core.frame.DataFrame'>
RangeIndex: 65079 entries, 0 to 65078
Data columns (total 7 columns):
 #   Column    Non-Null Count  Dtype 
---  ------    --------------  ----- 
 0     userID  65079 non-null  object
 1   Track     63736 non-null  object
 2   artist    57512 non-null  object
 3   genre     63881 non-null  object
 4     City    65079 non-null  object
 5   time      65079 non-null  object
 6   Day       65079 non-null  object
dtypes: object(7)
memory usage: 3.5+ MB
None
'''