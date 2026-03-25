#local vaariable has priority
result = 'A omelete está pronta!' # Declarada como uma variável global

def omelet(cheese, eggs_number):
    result = 'A omelete está pronta! Ovos usados: ' + str(eggs_number)
    if cheese == True:
        result = result + ', com queijo'
    else:
        result = result + ', sem queijo'
    print(result)

omelet(True, 3)
print(result)