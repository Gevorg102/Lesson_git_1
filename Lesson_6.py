print()

'''
sex = input('Gender (M/F): ').upper()
age = int(input('Age: '))
education = input('Education (H/M): ').upper()
work_exp = int(input('Work expirience: '))
res = sex =='M' and age >=18 and (education == 'H' or work_exp >2)
print('You entered', res)
'''

'''
x =4
res=not(x > 5 or x < 10)
print(res) #False
'''

'''
x = 5
y = 7
print(id(x))
print(id(y))
print(x is y)  # False
print(x is not y)  # True
print(x==y) # False
'''

'''
dasaran = 'ani, ashot, zack'
name = input('Name: ').lower()
res = name in dasaran
print(name, res)
'''

'''
makbook = 'pro, pro_x, z'
model = (input('model: '))
res = model in makbook
print(res)
'''
'''
cars = '15, opel, klorfar, 15'
date = '2008, 2015, 1998'
car = input('car name: ')
year = input('year: ')
res = car in cars and year in date
print(res, car, cars.count(car)) #count-@ qanakn e woroshum twyali 
'''

'''
kafe_name= 'maria, narek, armine, suren, armine'
name = input('name: ')
res = name in kafe_name
print(res, kafe_name.count(name))
'''

'''
banan = input('have you banan? (Yes/No): ').lower() == 'yes'
qiwi = input('have you qiwi? (Yes/No): ').lower() == 'yes'
orange = input('have you orange? (Yes/No): ').lower() == 'yes'
luys = input('luys@ (anj/miac): ').lower() == 'yes'
res_banan = banan and luys 
res_qiwi = qiwi and luys
res_orange = orange  and luys

print('banan: ', res_banan, 'qiwi: ',res_qiwi, 'orange: ',res_orange, 'luys: ',luys)
'''

'''
orange = input('Have you orange: ').lower() == 'yes'
light = input('Have you light: ').lower() == 'yes'
print('unenq orange', orange)
print('unenq light', light)

res_orange = orange and not light
print('hanumenq orange-@:  ', res_orange)
'''

'''
word = 'my city is Yerevan'
res = word.replace('Yerevan', 'Paris') # Yerevan -@ porxarinum e Paris -i
print(res)
'''

# print(abs(-18)) #  abs() ___ modul e darcnum e drakan tiv

num = int(input('gri tiv: '))
res2 = num // 100 #eranish tiv@
res1 = num // 10 % 10 #erknish
res = num % 10   # talu e werjin tiv@ || mianish
print(res2, res1, res)

