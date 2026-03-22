#whiout key's values
financial_info = {
    'American Express': 93.23,
    'Boeing': 178.44,
    'Coca-Cola': 45.15,
    'Nike': 97.99,
    'JPMorgan':96.27,
    'Walmart': 130.68 
}

walmart_price_1 = financial_info['Walmart']
walmart_price_2 = financial_info.get('Walmart')

print(walmart_price_1)
print(walmart_price_2)

# financial_info = {
#     'American Express': 93.23,
#     'Boeing': 178.44,
#     'Coca-Cola': 45.15,
#     'Walt Disney': 119.34,
#     'Nike': 97.99,
#     'JPMorgan':96.27,
#     'Walmart': 130.68 
# }

# #direcly accessing the value of a key
# print(financial_info['Walmart'])

# #using get() method to access the value of a key
# print(financial_info.get('Nike'))

# #creating alternative if value not found
# print(financial_info.get('Apple', 'Not Found'))

