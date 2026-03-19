#Composite assignment
items = 10

items += 5 # como items = items + 5
print(items)

items -= 5 # como items = items - 5
print(items)

items *= 3 # como items = items * 3
print(items)

items /= 5 # como items = items / 5
print(items)


#sum, max and min
movies_duration = [142, 175, 152, 195, 201, 154, 178, 139, 133, 126]

total_duration = sum(movies_duration) #soma todos os elementos da lista
max_duration = max(movies_duration) #obtêm o maior elemento da lista
min_duration = min(movies_duration) #obtêm o menor elemento da lista

print(total_duration)
print(max_duration)
print(min_duration)