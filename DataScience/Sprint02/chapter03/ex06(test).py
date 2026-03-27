'''Tarefa 2
Vamos torná-la ainda mais flexível! Escreva mais duas funções similares à anterior que chamamos:

filter_age() e
filter_income()
Na primeira função, usaremos a idade como o filtro, enquanto na segunda, vamos usar a renda como o filtro.

A lista clients deve ser usada como argumento para o parâmetro clients_list em ambas as funções, de forma parecida ao que você fez na tarefa anterior.

Ambas as funções devem filtrar os clientes com valores maiores do que o valor passado como um argumento na chamada da função.

Chame a função filter_age() e filtre a lista clients, extraindo os clientes que tenham mais de 40 anos. Armazene os resultados na variável filtered_age. 

Da mesma forma, chame a função filter_income() e filtre a lista clients, extraindo apenas os clientes que tenham uma renda maior que 250.000. Salve os resultados na variável filtered_income.

Imprima as variáveis filtered_age e filtered_income (que já estão no pré-código).'''


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

# escreva duas funções de filtragem aqui: filter_age e filter_income
def filter_age(clients_list, age):
    filtered_result = []
    for client in clients_list:
        if client[2] > age:
            filtered_result.append(client)
    return filtered_result

def filter_income(clients_list, income):
    filtered_result = []
    for client in clients_list:
        if client[3] > income:
            filtered_result.append(client)
    return filtered_result

filtered_age = filter_age(clients, 40)
filtered_income = filter_income(clients, 250000)

# imprime o resultado
print(filtered_age)
print(filtered_income)