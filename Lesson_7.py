'''
a = int(input('gri a: '))
b = int(input('gri b: '))
res =a**3 + 3 * a**2 *b +3*a*b**2 +b**3
print(res)
'''

'''
from math import factorial

fact = int(input('gri factoriali tiv: '))
print(factorial(fact))
'''

'''
n = input('gri tiv: ')

result = int(n) + int(n*2) + int(n*3) #n =5;  5 + 55 + 555
print(result)
'''

'''
rep = 'I am a Gevorg #'
res = rep.replace('#', 'Hi')
print(res)
'''

'''
num = int(input('gri tiv: '))
res = num>= 0
print(res)
'''

'''
name = input('gri anun@ nootbukneri: ')
notebooks = 'Hp, Hyper, Dell, Lenovo, Hyper, Hp'
res = notebooks.count(name)
print(res)
'''

'''
import random
num = input('numbers: ')

comp = random.randint(1,10)
res = str(comp) in num
print(comp, res)
'''

'''
gram = int(input('gri grami qanak@: '))

sig = gram//20
mn =gram %10
print(sig, 'mnacord: ',mn)
'''