name = 'Maggie'
age = 23
height = 157

print(name + " tem " + str(age) + " anos e " + str(height) + " cm de altura")
print(f"{name} tem {age} anos e {height} cm de altura") #F-strings
print("{} tem {} anos e {} cm de altura".format(name, age, height)) #format() method


#========================================================================================
# upper() — converts all characters to uppercase
# lower() — converts all characters to lowercase
# replace() — replaces parts of a string with another string
# strip() — removes leading and trailing spaces from a string

shopping_list = '''MAÇÃS
laranjas
leite
Maçãs
pão
Sorvete
maçãs
ÓLEO
Pão'''

shopping_list = shopping_list.lower()# converta a variável shopping_list para minúscula aqui
print(shopping_list)
print(shopping_list.replace('maçãs', 'banana')) # substitua 'maçãs' por 'banana' aqui

#===============

sentence = "   Python é uma linguagem de programação interpretada de alto nível, de uso geral.   "
new_sentence = sentence.strip()# primeiro, remova os espaços desnecessários
new_sentence = new_sentence.replace(' ', '-')# depois, substitua espaços por hifens (-)

print(new_sentence) #por fim, imprima a string resultante aqui


#==============================
user_input = " MaRaDoNa "

clean_input = user_input.upper().strip()

print(clean_input)
