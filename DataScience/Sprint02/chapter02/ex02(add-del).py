financial_info = {
    'American Express': 93.23, 
    'Boeing': 178.44, 
    'Coca-Cola': 45.15, 
    'Nike': 97.99, 
    'JPMorgan': 96.27, 
    'Walmart': 130.68, 
    'Walt Disney': 119.34
    }

#print each item of the dictionary with its respective value separated by :
print('Original Financial Information dictionary:')
for key, value in financial_info.items():
    print(f'{key}: {value}')
print(f'Total number of companies: {len(financial_info)}')

#check if the key 'walt disney' exists in the dictionary, if it does, update its value by adding 3.2, if it doesn't, add the key with the value 119.34
if financial_info.get('Walt Disney') == None: 
    financial_info['Walt Disney'] = 119.34 
else: # if its exists, we update the value by adding 3.2
    financial_info['Walt Disney'] += 3.2 


#add the key ''Microsoft' with the value 208.35
financial_info['Microsoft'] = 208.35
print(f'\n {'n'*40 } \nMicrosoft has been added to the dictionary\n\nDictionary:', f'Total items: {len(financial_info)}')

for key, value in financial_info.items():
    print(f'{key}: {value}')

#using dell to remove the key 'Nike' from the dictionary
del financial_info['Nike']
print('\n','-'*40,  '\nNike has been removed from the dictionary\n\nDictionary:', f'Total items: {len(financial_info)}')
for key, value in financial_info.items():
    print(f'{key}: {value}')

#using dell to remove the key 'Boeing' from the dictionary
Boeing_price = financial_info.pop('Boeing')
print(Boeing_price)#pop() method removes the last item from the dictionary and returns it, but since dictionaries are unordered, it may not remove 'Boeing' specifically. To remove 'Boeing', we should use pop('Boeing') instead.
print('\n','-'*40,  '\nBoeing has been removed from the dictionary\n\nDictionary:', f'Total items: {len(financial_info)}')
for key, value in financial_info.items():
    print(f'{key}: {value}')
