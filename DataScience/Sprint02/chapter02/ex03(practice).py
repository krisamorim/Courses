'''
Tarefa 1
A equipe de gestão ABC pediu que você reorganize a lista dos clientes de modo que eles possam acessar os dados com maior facilidade.

Seu objetivo é transformar cada lista da lista clients em um dicionário e então imprimir esse dicionário, antes de converter a próxima lista em um novo dicionário.

Use as seguintes chaves para cada dicionário que criar:

"id"
"client_name"
"age"
"yearly_income"
"work_field"
'''
# clients = [
#     [32456, "Jack Wilson", 32, 150000, "Healthcare"],
#     [34591, "Nina Brown", 45, 250000, "Telecom"],
#     [37512, "Alex Smith", 39, 210000, "IT"],
#     [39591, "Brian Perez", 29, 340000, "Transportation"],
#     [45123, "Sarah Lee", 28, 120000, "Marketing"],
#     [47635, "David Kim", 36, 180000, "Finance"],
#     [49571, "Samantha Chen", 42, 220000, "Retail"],
#     [50391, "Juan Rodriguez", 31, 160000, "Architecture"],
#     [34556, "Lucas Hernandez", 37, 75000, "Education"],
#     [64291, "Jessica Li", 25, 125000, "IT"],
#     [74512, "Emma Davis", 47, 197000, "Finance"],
#     [83191, "Sophia Perez", 34, 225000, "Transportation"],
#     [91023, "Liam Kim", 29, 98000, "Retail"],
#     [96435, "Ava Chen", 31, 175000, "Marketing"],
#     [100571, "Noah Rodriguez", 28, 85000, "Architecture"],
#     [101321, "Olivia Wilson", 44, 310000, "Telecom"],
#     [104556, "William Brown", 38, 289000, "Finance"],
#     [105491, "Emily Smith", 29, 193000, "Healthcare"],
#     [107512, "Michael Perez", 53, 415000, "Transportation"]
# ]

# for client in clients:
# 	# primeiro, crie um dicionário usando chaves
# 	new_client_dict = { 
#         "id": client[0],
#         "client_name": client[1],
#         "age": client[2],
#         "yearly_income": client[3],
#         "work_field": client[4]
#     }
# 	# em seguida, imprima o dicionário criado
# 	print(new_client_dict)
	
# # #another way to print the items with a number in front of them
# # for i, client in enumerate(clients, start=1):
# #     new_client_dict = { 
# #         "id": client[0],
# #         "client_name": client[1],
# #         "age": client[2],
# #         "yearly_income": client[3],
# #         "work_field": client[4]
# #     }
# #     if i < 10:
# #         print(f'0{i}º item: {new_client_dict}')
# #     else:
# #         print(f'{i}º item: {new_client_dict}')


#==========================================================================================================
'''
Tarefa 2
Desta vez, o departamento de marketing do ABC está interessado em saber o nível de renda para cada área de trabalho de
 seus clientes. Ele pediu para você coletar dados de renda dos clientes para cada área.

No pré-código, assim como na tarefa anterior, você vai ver a lista clients. Se você quiser dar mais uma olhada na lista, 
ela está aqui:
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

Além disso, no pré-código, inicializamos um dicionário chamado incomes_per_field (rendas por área). Seu objetivo é preenchê-lo. 
As chaves serão as áreas em que trabalham os clientes do ABC, e os valores serão listas com rendas de todos os clientes 
que trabalham em cada área correspondente. Aqui está um exemplo de um par chave-valor:
"Healthcare": [150000, 193000]

A chave é a área ("Healthcare"), ou seja, saúde), e os valores são duas rendas dos dois clientes da lista clients que 
rabalham em "Healthcare".

Para preencher o dicionário incomes_per_field, percorra a lista clients e extraia o nome da área e a renda para 
cada cliente. Em seguida, verifique se o nome extraído da área existe no dicionário incomes_per_filed:

Se não, adicione-o como uma chave e defina uma lista com uma única renda como um valor.
Se existir, adicione a renda à lista de rendas.

'''

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

incomes_per_field = {} # coloque aqui as rendas para cada área

for client in clients:
    # primeiro, extraia o nome da área
    field = client[4]
    # segundo, extraia a renda
    income = client[3]
    if field not in incomes_per_field:
        # adicione uma nova área como uma chave e defina uma lista como um valor
        incomes_per_field[field] = [income]
    else:
        incomes_per_field[field].append(income)

# não modifique o código abaixo. Ele imprime o resultado
print(incomes_per_field)