some = input('Type something\n')

#type
print('the type is {}\n'.format(type(some)),'='*20)

#is there only space?
if some.isspace():
  print('Only space\n','='*20)
else:
  print("not only space\n",'='*20)

#is numeric?
if some.isnumeric():
  print('Is numeric\n'+'='*20)
else:
  print("Not is numeric\n","="*20)

#is alphabetic
print('Is alphabetic:', some.isalpha())

#is alphanumeric
print("Is alphanumeric:", some.isalnum())

#is upper case, is lower case, is capitalized
print("Is upper case: {}\nIs lower case: {}\nIs capitalized: {}".format(some.isupper(),some.islower(), some.istitle()))
