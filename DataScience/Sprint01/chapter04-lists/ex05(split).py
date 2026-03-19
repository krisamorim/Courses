phrase = 'vamos dividir ou não vamos dividir'
words = phrase.split()
print(f'The value of the variable phrase is: {phrase} and the type of the variable is: {type(phrase)}')
print(f'The value of the variable words is: {words} and the type of the variable is: {type(words)}')
print(f'The length of the phrase is: {len(phrase)} anda the length of the list is: {len(words)}')


#======================================= Another example =======================================

phrase = 'Brilha-brilha-estrelinha-lá-no-céu-pequenininha'
words = phrase.split('-')
print(f'\nVariable phrase is: {phrase} ')
print(f'Variable words is: {words}')

#========= converte a string names em uma lista de nomes usando split() e imprima a lista resultante ==================
names = 'Jack Wilson,Nina Brown,Alex Smith,Brian Perez,David Martinez,John Kim'
names_split = names.split(",")# escreva seu código aqui
print(names_split)