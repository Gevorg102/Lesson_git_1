print()

#erku hat list nmaner@ inchqan en

'''
list = [48, 45, 22, 35485748, 0, 1215 ]
list2 = [48, 87714, 0, 3548222, 2, 3 ]

res = [i for i in list if i in list2]
a = len(res)
print(a)
'''

# list1 -@ uni 10 hat tiv erkordy 11 hat meky petq e tarberwi gtni ayd tiv@

'''
list = [45, 2, 3, 78, 15, 78, 731, 6, 8, 69]
list2 = [45, 2, 3, 78, 181, 78, 731, 6, 8, 69, 15]
'''

# petq gres parol menak 8 qanakutyamb cankacac nshanow

'''
import string

while True:

    pas = (input('gri parol@ (1-8): '))
    count = 0
    symbol = 0

    if len(pas) < 8:
        print('length password must be great than 8')
        continue
    if pas[0].islower():
        print('First length of tha password must be upper')
        continue
    for i in pas:
        if i.isdigit():
            count +=1
        elif i in string.punctuation:
            symbol+=1

    if count < 2:
        print('Number of tha password must be two')
        continue
    if symbol < 2:
        print(('Symbol of tha password must be two'))
        continue

    print('Strong')
    break

'''

# grenq bar wori hakarak dzew@ nuyn dzwowo kardacwi ev ta True

'''
while True:
    text = input('gri bar: ')
    if text == text[::-1]:

        print(True)
'''

# grumenq cragir wor@ string@ kdarcni list


'''
str = 'my string'

str = str.split(',')

print(type(str))
'''

# gri list zuyq ev kent twerow bayc cuyc ta menak kenter@

list = [48, 12, 31, 8, 16, 731, 181, 81, 20]

        
'''
res = [i for i in list if i%2!=0]
print(res)
'''

'''
count =0

for i in range(len(list)):
    if list[count] %2==0:

        list.remove(list[count])
        count-=1
    count+=1
print(list)
'''