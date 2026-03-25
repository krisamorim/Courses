'''O trecho de código abaixo contém operações repetitivas. Especificamente, ele calcula o total, multiplicando o número de itens pelo seu preço. Podemos dar um desconto de 10% se a quantidade for maior do que 5. Fazemos isso multiplicando o total por 0,9. Seu objetivo é escrever uma função chamada calculate_total_price que elimine a redundância e que possa ser usada para todos os três casos apresentados abaixo.'''

# escreva seu código aqui para definir uma função
def calculate_total_price(price, quantity):
    item_total = price * quantity
    if quantity > 5:
        item_total = item_total * 0.9
    return item_total


# Defina os preços e as quantidades dos três itens
item_price_1 = 20.0
item_quantity_1 = 20

item_price_2 = 30.0
item_quantity_2 = 1

item_price_3 = 10.0
item_quantity_3 = 6


# Chame a função para cada item e armazene o resultado em uma variável
item_total_1 = calculate_total_price(item_price_1, item_quantity_1)
item_total_2 = calculate_total_price(item_price_2, item_quantity_2)
item_total_3 = calculate_total_price(item_price_3, item_quantity_3)


# Imprima o preço total de cada item no carrinho
print(item_total_1)
print(item_total_2)
print(item_total_3)
