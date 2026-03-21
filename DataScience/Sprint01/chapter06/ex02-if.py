weather = 'sol'

# condição
if weather == 'chuva':
    print('leve um guarda-chuva')
else:
    print('leve um chapéu')
print('vamos lá!')

#==================searching in substring===========================
quote = "O progresso é impossível sem mudança, e aqueles que não conseguem mudar suas mentes não conseguem mudar nada."
if "ogres" in quote:
    print("Onde há progresso, há ogres!")
else:
    print("Aqui não, docinho de coco!")



#=============================================
weather = 'chuva'

if weather == 'chuva':
    item_to_take = 'guarda-chuva'
if weather == 'sol':
    item_to_take = 'chapéu'
if weather == 'neve':
    item_to_take = 'gorro e um cachecol'
else:
    item_to_take = 'nada'

print(weather)
print(item_to_take)