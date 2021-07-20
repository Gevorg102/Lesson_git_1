
'''
cars = 'audi, bmw'

if 'audi, bmw' in cars:
	print('yes')
'''


'''
cars = ('bmw','audi', 12, 123.3245, True,(1,515,2))
print(len(cars)) # ays depqum 'len'-@ elementneri qanakn e stugum

print(515 in cars[-1]) # ete tvyal elementy parunakum nshvac objectum True hakarak depqum False
print('yes')
'''

# a = ()
# print(type(a))

# c = tuple()
# print(type(c))


# x = 2
# print(type(x))

# print(x.__sizeof__())




# test = tuple(range(1,1000))
# print(test.__sizeof__())


# fruits = 'Bananna','apple','orange','apple'


'''
print(fruits.count('apple'))

if 'Bananna' in fruits:
    print('yes')  #ete ka tvyal objekty apa meji hramany katarelu  e
    print(type(fruits))
	
else:
	print('no')



for f in fruits:
	print(f)
    
	if f == 'apple': #ete nshvac strokan ka objectum apa dranic heto kkatari ira mechi hramaner@          
    		break
'''


fruits = 'Bananna','apple','orange','qiwi'



# print(fruits[0:3])

print(fruits[1:3])

# print(fruits[-1])

# print(fruits[-3:-1])

# # print(fruits[::]) ## bolorn e cuyc talu

# print(fruits[:-2]) ## ete skzbiny ches nshum inqy awtomat amen arajin e cuyc talu

# print(fruits[0::2]) ## nshvac objectnerna menak nshelu

# print(fruits[::-1])

# print(fruits[1:5:2])

# print(fruits[-4::2])


'''
name = 'hak','gag','vax','edo' # darnume worpes elementneri qanakic kaxwac tiv

c = 0
for i in name:
	c += 1

print(c) # 4
'''



'''
fruits = 'Bananna','apple','orange','qiwi'

for i in range(len(fruits)):
	if fruits[i] == 'apple':
		print(i)
		break

c = 0
for i in fruits:
    if i =='apple':
        break
    c+=1
print(c)
'''

'''
tuple1 = ('a',2, 'c')
tuple2 = (1,2,3)
tuple3 = tuple1 + tuple2
print(tuple3)
'''


'''
## Напишите программу на Python для подсчета элементов в списке до тех пор, пока элемент не станет кортежем.

num = [1,2,[10,478,47,474,4720],8,(485,5),48]
c = 0
for n in num:
	if isinstance(n,tuple): ##stugum e elementneri qanaky minchew yntrvac 'class' hasnel@
		break
	c += 1
print(c)
'''


'''
tup = ('e','x','e','r','c','i','s','e','s')
mystr = ''.join(tup)
print(mystr)
'''


	
'''
tup = (1,5,6,8,'f',5,'w',8)
c = 0
x = 0
for i in tup:
	if isinstance(i,int):
		c += i #integerneri gumarum@
		x += 1 #qanaky yst indzexi
y = c / x
print(y)
'''   


'''
x = 12,2122,31,42

print(sum(x))
print(min(x))
print(max(x))
'''
