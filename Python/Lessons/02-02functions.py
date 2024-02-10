#doing root square and round up
from math import sqrt, ceil
number01 = int(input("Enter a number: "))
print(" The square root of {} is {}\nRound up is {}".format(number01, sqrt(number01), ceil(sqrt(number01))))

Documentação
#https://docs.python.org/3/

#modulo matemático
#import math
from math import sqrt, ceil, floor
num = int(input('Digite um número: '))
raiz = sqrt(num)
print('A raiz de {} é {:.2f}\nArredondadno para cima é {}\nArredondadno para baixo é {}'.format(num, raiz, ceil(raiz), floor(raiz)))
print('_'*25)
print('\n')

#numero aleatórios
import random
num = random.random()
print(num)

#randomizar numeros inteiros entre 1 e 10
numInt = random.randint(1,10)
numIntSegundo = random.randint(1,10)
print('O 1º número aleatório é {}, o 2º é {}'.format(numInt, numIntSegundo))

#módulos de emoji
import emoji
print(emoji.emojize("Python é :polegar_para_cima:", language='pt'))