print()

a =27
b =14
c =12
d=25
'''
if b > a :
    print('b is big')
elif a > b:
    print('a is big')
else:
    print('havasar en')
'''

'''
if a>b and d>c:
    print('a and d are bigger')
'''

'''
num = float(input('Enter a number: '))
if num >=0:
    if num == 0:
        print('Zero')
    else:
        print('Positive number')
else:
    print('Negative number')
'''

'''
res = None
if res is True:
    print('None is True?')
elif res is False:
    print('None is False?')
else:
    print('None is not True, False')
'''

# a = input('greq inch wor bar: ')
'''
if a.isalpha(): # isalpha() __ menak tarerri hamara
    print('yes')
else:
    print('No')
'''

'''
if a.isdigit(): # isdigit() __ menak tveri hamara
    print('yes')
else:
    print('No')
'''

'''
if a.isalnum(): # isalnum() __ nshaner chi kareli
    print('yes')
else:
    print('No')
'''

'''
if a.istitle():  # istitle() __ arajin tar@ petq a mecatar gri mnacac depqum 'No'
    print('Yes')
else:
    print('No')
'''
'''
if a.isupper(): # isupper() __ stuguma te bolor tarer@ mecatara te che
    print('yes')
else:
    print('No')

if a.islower(): # islower() __ stuguma te bolor tarer@ poqratara te che
    print('yes')
else:
    print('No')
'''

''' print(a.capitalize()) # bari arajin tar@ sarquma mecatar mnacac@ poqratar '''

# useric uzumes tariq ete chi asum zgushacnumes

# age = input('Tariqt asa: ')

'''
if age.isdigit():
    print('shnorhakalem')

#     if int(age)> 0:
#         print('shnorhakalem')
# else:
#     print('Positive gri')


else:
    age = input('Tariqt asa: ')
    if age.isdigit():
        print('shnorhakalem')
    else:
        print('asumem tariqd asa')
'''

#2 ==10.5 amen tari +4

shun =10.5

age_dog = int(input('gri shan tariq@: '))
if age_dog > 0 and age_dog < 2:
    human_age = 5.25 *age_dog
else:
    if age_dog >2:
        dog = 10.5 +(age_dog-2)*4
    print(dog)


print('human age: ', dog)
