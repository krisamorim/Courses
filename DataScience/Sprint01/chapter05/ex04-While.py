# Valores aleatórios podem ser atribuídos a variáveis usando a função randint() da biblioteca random. 
# A função randint gera números inteiros aleatórios dentro de um intervalo especificado.
# Portanto, vamos declarar o intervalo de 30 a 120 e simular o peso de uma pessoa aleatória.

from random import randint # importamos a função randint da biblioteca random

capacity = 400 # capacidade do elevador em kg
total_weight = 0 # variável que armazena o peso total

while total_weight < capacity: # enquanto o peso total é menor do que a capacidade máxima
    person_weight = randint(30, 120) # geramos um número aleatório de 30 a 120
    total_weight += person_weight # o peso gerado é adicionado ao peso total que será impresso
    print(f'Uma pessoa entra. Carga do elevador: {total_weight}')
    
print('Desculpe! O elevador está lotado. Você terá que esperar pelo próximo.')


#================ another example ==================
num_people = 0 # começa em 0 e não há ninguém dentro
capacity = 10 # variável que armazena o limite de pessoas

while num_people < capacity: # enquanto o número de pessoas é menor que a capacidade máxima
    num_people += 1 # uma pessoa entra
    print(f'Uma pessoa entra. Carga do elevador: {num_people}')
    
print('Desculpe! O elevador está lotado. Você terá que esperar pelo próximo.')



#================ another example ==================
from random import randint

capacity = 400 # capacidade do elevador em kg
total_weight = 0 # variável que armazena o peso total
num_people= 0 # começa em 0, não tem ninguém dentro

while total_weight < capacity: # enquanto o peso total é menor do que a capacidade máxima
    person_weight = randint(30, 120) # geramos um número aleatório de 30 a 120
    total_weight += person_weight # o peso gerado é adicionado ao peso total
    num_people += 1 # uma pessoa entra
    print(f'Uma pessoa entra. Carga do elevador: {total_weight}')
    
print(f'Desculpe! O elevador está lotado. Você terá que esperar pelo próximo. \n{num_people} pessoas já estão no elevador')
