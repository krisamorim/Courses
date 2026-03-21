# movies_info = [
#     ['The Shawshank Redemption', 'USA', 1994, 'drama', 142, 9.111],
#     ['The Godfather', 'USA', 1972, 'drama, crime', 175, 8.730],
#     ['The Dark Knight', 'USA', 2008, 'fantasy, action, thriller', 152, 8.499],
#     ["Schindler's List", 'USA', 1993, 'drama', 195, 8.818],
#     ['The Lord of the Rings: The Return of the King', 'New Zealand', 2003, 'fantasy, adventure, drama', 201, 8.625],
#     ['Pulp Fiction', 'USA', 1994, 'thriller, comedy, crime', 154, 8.619],
#     ['The Good, the Bad and the Ugly', 'Italy', 1966, 'western', 178, 8.521],
#     ['Fight Club', 'USA', 1999, 'thriller, drama, crime', 139, 8.644],
#     ['Harakiri', 'Japan', 1962, 'drama, action, history', 133, 8.106],
#     ['Good Will Hunting', 'USA', 1997, 'drama, romance', 126, 8.077]
# ]

# movies_filtered = [] # lista vazia para armazenar o resultado

# for movie in movies_info: # iterando sobre as linhas da tabela original
#     if movie[4] > 180: # se um filme dura mais do que 180 min
#         movies_filtered.append(movie) # adicione a linha à lista movie_filtered

# for movie in movies_filtered: # imprimindo o conteúdo da lista movies_filtered
#     print(movie) 

# #===============================================================================

# movies_filtered = []

# for movie in movies_info:
#     if movie[2] == 1994 or movie[-1] < 8.5:
#         movies_filtered.append(movie)

# # não modifique o código abaixo, pois ele imprime o resultado final
# for movie in movies_filtered:
#     print(movie) 


# #===============================================================================

clients = [
    [32456, "Jack Wilson", 32, 150000, "Healthcare"],
    [34591, "Nina Brown", 45, 250000, "Telecom"],
    [37512, "Alex Smith", 39, 210000, "IT"],
    [39591, "Brian Perez", 29, 340000, "Transportation"],
    [45123, "Sarah Lee", 28, 120000, "Marketing"],
    [47635, "David Kim", 36, 180000, "Finance"],
    [49571, "Samantha Chen", 42, 220000, "Retail"],
    [50391, "Juan Rodriguez", 31, 160000, "Architecture"],
    [34556, "Lucas Hernandez", 37, 75000, "Education"],
    [64291, "Jessica Li", 25, 125000, "IT"],
    [74512, "Emma Davis", 47, 197000, "Finance"],
    [83191, "Sophia Perez", 34, 225000, "Transportation"],
    [91023, "Liam Kim", 29, 98000, "Retail"],
    [96435, "Ava Chen", 31, 175000, "Marketing"],
    [100571, "Noah Rodriguez", 28, 85000, "Architecture"],
    [101321, "Olivia Wilson", 44, 310000, "Telecom"],
    [104556, "William Brown", 38, 289000, "Finance"],
    [105491, "Emily Smith", 29, 193000, "Healthcare"],
    [107512, "Michael Perez", 53, 415000, "Transportation"]
]

# listas vazias para adicionar clientes
standard = []
plus = []
elite = []
executive = []

for client in clients:
    if client[3] < 100000:
        standard.append(client)
    elif client[3] >= 100000 and client[3] < 200000:
        plus.append(client)
    elif client[3] >= 200000 and client[3] < 300000:
        elite.append(client)
    elif client[3] >= 300000:
         executive.append(client)

print(executive)

standard_young = []
plus_young = []
elite_young = []
executive_young = []

for client in clients:
    if client[3] < 100000 and client[2] < 40:
        standard_young.append(client)
    elif client[3] >= 100000 and client[3] < 200000 and client[2] < 35:
        plus_young.append(client)
    elif client[3] >= 200000 and client[3] < 300000 and client[2] < 35:
        elite_young.append(client)
    elif client[3] >= 300000 and client[2] < 35:
        executive_young.append(client)
