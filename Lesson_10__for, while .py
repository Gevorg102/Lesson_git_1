
'''
names = ['Artur', 'Vahag', 'Ani']
for anun in names:
    print(anun)
'''

'''
names = 'Aramajis'
for name in names:
    print(name)   # tarer@ amen toxuma grum
'''
'''
name = 'Xachatur'
for i in name:
   
    if i =='r':
        break 
    print(i) # tpelu e minchew nshvac taric naxord tar@
'''

'''
name = 'Xachatur'
for i in name:
   
    if i =='c' or i =='h':    #nshvac nshaner@ chi tpum
        continue
    print(i) 
'''

'''
for i in range(4): #qayleri qanaky
    num = int(input('Gushakir tiv@: '))
    if num== 3:
        print('you win')
        break
    else:
        print('wrong answer')
'''

'''
for i in range(0, 100, 2): # 0-100 twer@, 2 avelacnelow
    print(i)
'''
'''
name = 'Haykush'
name = iter(name)
print(next(name)) #H
print(next(name)) #a
print(next(name)) #y
print(next(name)) #k
print(next(name)) #u
print(next(name)) #s
print(next(name)) #h


# try:
#     print(next(name))
# except:
#     print('end')   
'''

'''
for i in range(10):
    pass #baca toxum

'''
'''
for i in '♠♣♦♥':  #global-um inchqan nishes grum aydqan katarelua trac hraman@
    for j in 'JQKT':
        print(i, j)
'''

'''
while True:
    x=6
    num = int(input('number: '))
    if num ==x:
        print('win')
        break
    else:
        print('lose')
while True:
    print('hi') #ete 'break' chka anverj katarelu e hraman@
'''
    
'''
i = 1
while i < 6:
    i +=3
    print(i)
    i -=1
'''

'''
import time 
while True:
    localtime = time.localtime()
    result = time.strftime('%I:%M:%S  %p', localtime)
    print(result)
    time.sleep(1)
'''

'''
tar = 'bararan'
qan = 0

for i in tar:
    if i =='a':
        qan+=1
print(qan)
'''

'''
import time
import os
res = 0
while True:
    os.system('clear')
    res +=1
    print('\n' *14, ' '*43,res)
    time.sleep(1)
'''

import random
es = 0
pc = 0
while True:
    i = int(input('num: '))
    p = random.randint(1, 3)
    if i==p:
        print(i, 'rand: ',p)
        es += 1
    else:
        print(i, 'rand: ',p)
        pc +=1
    if es ==3:
        print('ok Arno', es, pc)
        break
    elif pc ==3:
        print('ok pc', pc, es)
        break
    
