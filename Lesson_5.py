'''
import string



letters = string.ascii_letters #a-Z tarer@

lower = string.ascii_lowercase # poqratar@ 

upper = string.ascii_uppercase # mecatar tarer@

numbers = string.digits # tver@

chars = string.punctuation # bolor shannern e cuyc tali

print(letters)
print(lower)
print(upper)
print(numbers)
print(chars)
'''

'''
import math

print(math.sqrt(16))
print(math.pi)
print(math.factorial(5))
'''

'''
from math import *

print(pi)
print(e)
print(sqrt(64))
'''
'''
import math 

print(math.ceil(1.2))  # 2
print(math.floor(0.7))  # 0
print(math.pow(4, 3))  # 64
print(round(1.486, 2))  # 1.49
print(format(4332.456, '.1f'))  # 4332.46
'''

# import random

'''
print(random.random())  # 0 ic 1 tver@
print(random.randint(0, 10)) #0-ic minchew 10
'''

'''
i = random.randint(1,6)
Friend = random.randint(1,6)
res = i > Friend

print(i, Friend, res)
'''

'''
x = 'few48fe'
print(random.choice(x))  #nshaneric mekn e yntrum
'''

'''
import random as ra

print(ra.randrange(0, 150, 2))
'''

'''
import time
print('Hi Me')
time.sleep(3)  # kompilacia e anum snhvac jamanak heto
print('Hi Alisa')
'''

# import os
'''
print(os.getcwd())
path = f'{os.getcwd()}/ folder' #papkaji anun@
os.mkdir(path) #stexcum e papkan
os.chdir(path)
os.rename('folder', 'fe')
'''
'''
import calendar
y = int(input('input the year: '))
m = int(input('input the month: '))
print(calendar.month(y,m))
'''
import datetime
'''
x = datetime.datetime.now()
print(x)
print(datetime.date.today())

x = datetime.datetime(2020, 5, 13, 10, 12, 5)
print(x)
'''

'''
x = datetime.datetime(1998, 5, 10, 16, 05, 04)
print(x- datetime.datetime.today())
'''
'''
x = datetime.datetime.now()
print(x.year)
print(x.strftime('%A'))
'''

