'''
def test():
    text = 'Hello function'
    print(text)
test()
'''

'''
def about_me(name, age):
    text = f'my name is {name}, I am {age} years old'
    print(text)
# name = input('What is your name: ')
# age = int(input('What is your name: '))

# about_me(name, age)
about_me(age = 18, name= 'Gev')
'''

'''
def my_country(name, country = 'Armenia'):
    about_me = f'My name is {name}, I am from {country}'
    print(about_me)

my_country('Bob', 'Sweden')
my_country('Bob', 'Germany')
my_country('Bob')
'''

'''
def my_function(fruits) :
    for mirq in fruits:
        print('Fruit', mirq)

my_list = ['apple', 'qiwi', 'cherry']
my_function(my_list)
'''



'''
def number():

    while True:    
        num = input('write number: ')
        if num.isdigit():
            num = int(num)
            return num
        else:
            print('Only number')

def gorcoxutyun():
    gorc = ('+', '-', '/', '*')
    while True:
        ch = input(gorc)
        if ch in gorc:
            return ch
        else:
            print('only', gorc)

def result():
    x = number()
    z = gorcoxutyun()
    y = number()

    if z =='+':
        return f'{x} +{y} = {x + y}'
print(result())
'''

'''
def test(*args): #verdarcnum e wopres  'Tuple'
    print(type(args))
    for i in args:
        print(i)
test(1, 1, 4731, 48, 248, 487, 9)
'''
'''
def Kwargs(**kwargs): #verdarcnum e wopres  'Dicitnory'
    print(type(kwargs), kwargs) 
Kwargs(name = 'Bob', age =21, car = 'BMW')
'''

# lambda
'''
lam = lambda y,x : x-y
print(lam(2, 5))
'''
    #Generatorner
    #map, filter, reduce
    
# def test(x):
#     return x**2
# print(list(map(test, range(1, 10))))

# generatorow
#print(list(map(lambda x: x**2, range(1, 10))))

#print(list(map(lambda x: x**2, filter(lambda x: x%2!=0, range(1, 10)))))  #filter -filtracnum bolor 'False' hramaner@

'''
from functools import reduce

def add(x,y):
    if y > 1000:
        y *= 0.11 
    else:
        y*=0.7
    res = x+y
    result = f'{x} + {y} ={res}'  ## cuyc e talis te 
    print(result)                 ## wonc e hramany katarum
    return res

my_list = [15, 21, 315, 148748]  # amen mi cucak hashwum e ev patasxany undunum worpes 'x' isk 'y'-@ hajord cucaki hamar@
res = reduce(add, my_list)
print(res)
'''
