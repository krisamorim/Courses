# word = 'supercalifragilisticexpialidocious'
# letter = word[5] # extraindo o 6º caractere de uma string
# print(letter)

# print("\nnegative indexing")
# last_letter = word[-1] # extraindo a última letra
# third_from_end = word[-3] # extraindo o terceiro caractere do final
# print(last_letter, third_from_end)

# phrase = 'Olivia loves her little yellow duckling'
# print(phrase[len(phrase) - 1])# imprima aqui o último caractere usando a função len() e indexação positiva
# print(phrase[-len(phrase)])# imprima aqui o último caractere usando a função len() e indexação negativa

string = 'In some ways, programming is like painting. You start with a blank canvas and certain basic raw materials. You use a combination of science, art, and craft to determine what to do with them' 

# obtenha e imprima o quarto elemento pelo índice aqui
print(string[3])
# obtenha e imprima o 4º elemento usando indexação negativa aqui
print(string[-len(string) + 3])# não era isso 
print(string[-4]) #era isso qeu queria