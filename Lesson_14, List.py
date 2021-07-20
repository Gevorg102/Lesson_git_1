'''
my_list = 'Hay Word, grgr'
my_list = my_list.split()
my_list1 = my_list.split(',')
print(my_list)
print(my_list1)
'''

'''
fruits = ['banan', 'qiwi', 'mango']
fruits[1] = 'apple'
print(fruits)
'''

'''
my_list = list(range(100)) #kta 0-ic minchew 99 tver@ neraryal
print(my_list)
'''

'''
fruits = ['banan', 'qiwi', 'mango']
fruits.append('orange')
print(fruits)
'''

'''fruits = ['banan', 'qiwi', 'mango']
fruits.insert(1, 'orange') #kta worpes nshvac tvi indexi sharqum avelacnelu
print(fruits)'''

'''
fruits = ['banan', 'qiwi', 'mango']
fruits.remove('qiwi') #jnjum e
print(fruits)
'''

'''
fruits = ['banan', 'qiwi', 'mango']
test = fruits.pop(1) #hanum e nshvac indexow elementy u darcnum string

print(fruits)
print(test)
'''

'''
fruits = ['banan', 'qiwi', 'mango']
del fruits[2] #nshvac@ indexow@ jnjum e,  ete indexy nshvac chi bolor elementnern e jnjum
print(fruits)
'''

'''
fruits = ['banan', 'qiwi', 'mango']
numbers = [48, 48, -8847.48, 4897]
fruits.extend(numbers) #nshvac parametrerow elementner@
print(fruits)
'''

'''
numbers = [48, 21, -8847.48, 4897]
numbers.sort()  # poqric mec
numbers.reverse() # fracnum e
print(numbers)
'''

'''
list1 = [1, 'Text', (48, 221)]
list2 = [1, 'Text', (48, 221)]
print(list1 == list2) # True
print(list1 is list2) # False,   qani wor id ner@ chi hamapatasxanelu qani wor integer chen
'''

'''

res = [i for i in range(10)]

print(res)


c = []
for i in range(10):  #kta nuyn hraman@
    c.append(i)
print(c)
'''

# res = [i for i in 'Aram' if i=='A'] 
# print(res)  ## A

'''
my_list = []
for i in range(100):
    if i % 2 ==0:
        my_list.append(i**2)
        
print(my_list) #zuyg tveri qarakusin
'''


'''
res = [i**2 for i in range(100) if i %2==0]
print(res)
'''

'''
res = [i if i%2 ==0 else -1 for i in range(100)]
print(res)
'''

'''
my_list = []
for i in range(100):
    if i % 2 ==0:
        my_list.append(i)
    
        my_list.append('-1')
print(my_list)
'''


'''
my_list = [4, 2, 22, 5, 5, 6, 7, 5]
for i in my_list:
    c = my_list.count(i)
    print('number: ', i, c, 'times')
'''


