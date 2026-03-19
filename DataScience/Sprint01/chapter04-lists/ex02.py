#append(), extend(),  insert() e pop()
#append() - adiciona um elemento ao final da lista
lista = [1, 2, 3]
lista.append(4)
print(lista) # [1, 2, 3, 4]

#extend() - adiciona os elementos de uma lista a outra
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista1.extend(lista2)
print(lista1) # [1, 2, 3, 4, 5, 6]
#-------------------------
row = [1, 2]
row.extend([3, 4])
print(row)

#insert() - adiciona um elemento em uma posição específica da lista
lista = [1, 2, 3]
lista.insert(1, 4)
print(lista) # [1, 4, 2, 3]

#pop() - remove um elemento da lista e retorna o valor removido
lista = [1, 2, 3]
valor_removido = lista.pop(1)
print(lista) # [1, 3]
print(valor_removido) # 2

titanic_movie = ['Titanic', 'USA', 1997, 'drama', 194]
# adicione o nome do diretor antes do gênero do filme
titanic_movie.insert(3, 'James Cameron')
print(titanic_movie)