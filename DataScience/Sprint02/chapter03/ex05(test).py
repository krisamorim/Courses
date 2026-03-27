'''Tarefa 1
Vamos começar escrevendo uma função chamada filter_clients para filtrar a lista de clientes por área de trabalho. A função vai receber dois parâmetros: clients_list (a lista de clientes) e field (o campo com a área de trabalho que a função precisa encontrar). A função vai iterar sobre cada cliente na lista, e se ela encontrar o cliente com a área de trabalho especificada na lista, a informação sobre o cliente será adicionada a uma nova lista. Essa lista será retornada como resultado da execução da função quando ela finalizar sua execução.

Chame a função para a área "Transportation", para fazer um teste. Em seguida, imprima a lista filtrada (já no pré-código).'''

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


# crie sua função filter_clients aqui
def filter_clients(clients_list, field):
    filtered_clients = []
    for client in clients_list:
        if client[4] == field:
            filtered_clients.append(client)
    return filtered_clients

filtered_list  = filter_clients(clients, "Transportation")

# imprimimos o resultado aqui
print(filtered_list)