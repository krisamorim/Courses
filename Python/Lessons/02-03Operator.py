#Using operators

n1 = float(input('Type some number\n'))
n2 = float(input('Type another number\n'))
print('{}\nThe first number is {:.0f} and second is {:.0f} \n{}\nthe division is {}\nthe entire division is {}\nthe rest of division is {}\nthe multiplication is {}\nthe subtraction is {}\nthe sum is {}\nthe average is {}\nthe square root is {:.3f}\nthe cubic root is {:.2f}\nthe power is {}'.format('='*20,n1,n2,'='*20,n1/n2,n1//n2,n1%n2,n1*n2,n1-n2,n1+n2,(n1+n2)/2,n1**(1/2),n1**(1/3), n1**n2))


"""
Precedence order:
1- ()
2- **
3- *  /  //  %
4- +  -

3*5+4**2 = 31
3*(5+4)**2 = 243
"""


#measure calculator
"""
value = float(input('Enter the qty in meters:\n'))
km = value / 1000
hm = value / 100
dam = value / 10
dm = value *10
cm = value * 100
mm = value * 1000
print('{:.0f}m in:\nkilometer is: {}\nhectometer is: {}\ndecameter is: {}\ndecimeter is: {}\ncentimeter is: {}\nmillimeter is: {}'.format(value, km, hm, dam, dm, cm, mm))
"""
