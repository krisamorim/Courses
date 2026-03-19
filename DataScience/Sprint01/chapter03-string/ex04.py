#slicing
city = 'Rio de Janeiro, Brasil'
substring = city[7:14]
print(substring)



#==========================================================================

#Print each letter of the city's name and place a number next to it, on the same line, separating them with commas.
for i in range(len(city)):
    print(i, city[i], end=', ')
    if i == len(city) - 1:
        print() # Imprime uma nova linha após o último caractere

print(city[4:1000])
print(city[-15:500])
print(city[4:0])

print(city[:14]) # instead of city[0:14]
print(city[16:]) #instead of city[16:22]