# Tarefa 2
# O departamento de marketing do Banco ABC tem interesse em saber a idade média dos clientes. A idade média é apenas a soma das idades de todos os clientes dividida pelo número de clientes. Use o ciclo for para iterar na lista de clients e atualize as variáveis total_age e num_clients em cada iteração do ciclo.
    
# A variável total_age deve armazenar a soma das idades, enquanto a variável num_clients é usada para armazenar o número total de clientes.

# As variáveis total_age e num_clients já estão declaradas para você fazer seus cálculos com elas. Após revisar a lista e atualizar essas duas variáveis, calcule a idade média de todos os clientes, armazene o resultado na variável average_age e imprima-o.
clients = [
    [32456, "Jack Wilson", 32, 150000, "Healthcare"],
    [34591, "Nina Brown", 45, 250000, "Telecom"],
    [37512, "Alex Smith", 39, 210000, "IT"],
    [39591, "Brian Perez", 29, 340000, "Transportation"],
    [45123, "Sarah Lee", 28, 120000, "Marketing"],
    [47635, "David Kim", 36, 180000, "Finance"],
    [49571, "Samantha Chen", 42, 220000, "Retail"],
    [50391, "Juan Rodriguez", 31, 160000, "Architecture"]
]

total_age = 0
num_clients = 0

for client in clients:
    total_age += client[2]   # idade
    num_clients += 1

average_age = total_age / num_clients

print(average_age)

#==============================================================================

# Tarefa 3
# A gerência está interessada em saber quando um cliente atinge um milhão em receita total e pediu que você escreva um código que calcule o número de anos necessários para um cliente atingir esse número. Para começar, ela pediu para escrever um código teste para 'Jack Wilson', que ganha 150000 por ano. Escreva um ciclo while que soma a receita anual total de Jack até que ele atinja 1 milhão. Assim que chegar lá, imprima o número de anos que levou para atingir essa receita total.

annual_income = 150000  # Receita anual de Jack
target_income = 1000000  # meta de receita

total_income_sum = 0  # receita total acumulada
years_to_million = 0  # número de anos

while total_income_sum < target_income:
    total_income_sum += annual_income
    years_to_million += 1

print(years_to_million)