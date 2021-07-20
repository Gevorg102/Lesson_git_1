print()


'''
num = int(input('gri qaranish tiv: '))
res3 = num //1000
res2 = num // 100 % 10 #eranish tiv@
res1 = num // 10 % 10 #erknish
res = num % 10   # talu e werjin tiv@ || mianish
result = str(res) + str(res1) + str(res2)+ str(res3)
print(int(result))
'''

'''
num = int(input('gri tvanish: '))

if num > 999 and num< 10000:
    print('qaranish')
elif num > 99 and num< 1000:
    print('qaranish')
elif num > 9 and num < 100:
    print('qaranish')
elif num > 1 and num < 10:
    print('mianish')
else:
    print('urish ban')
'''


'''
import random

qayl_user = input('qar, tuxt, mkrat: ')
pc = ('mkrat', 'tuxt', 'qar')
qayl_pc=random.choice(pc)
print(qayl_pc)
if (qayl_user =='qar' and qayl_pc =='mkrat') or (qayl_user =='mkrat' and qayl_pc =='tuxt') or (qayl_user =='tuxt' and qayl_pc =='qar'):
    print('you win')
elif qayl_user ==qayl_pc:
    print('nichya')
else:
    print('pc win')
'''

'''
time = 3
pc = 12
a = pc /time
user = a * 1.1

print(user)
'''

import random

user = int(input('gri folwerid qanaky (1-1000): '))
pc_fol = random.randint(1, 1000)


if user <=pc_fol:
    res = pc_fol *1.2
    if res>= user:
        print('bloger is pc')
    else:
        print('bloger is user')
else:
    print('havasar')
