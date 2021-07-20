"""
a = int(input('greq tiv: '))
res = a % 2 == 0

print( res)
"""

'''
people = int(input('qani mard petq e lini: '))
groups = int(input('qani mard ka xmbum?: '))
groups = people // groups
balance = people % groups
print('registered people _', balance, people, '\ngroups _ ', groups, '\nBalance_', balance)
'''

'''
tob = int(input('tobacco: '))
box_sigaret = 20
one_sigaret = 14
all_sigaret = tob //one_sigaret
tob_balance = tob % one_sigaret
all_box = all_sigaret// box_sigaret
sigaret_balance = all_sigaret % box_sigaret
print('Tobacco', tob, '\nbox sigaret: ', box_sigaret, '\nmi hat sigaret: ', one_sigaret)
print('sax sigarety', all_sigaret, '\ntobaco_balace: ', tob_balance, '\nmi hat sigaret: ', one_sigaret, '\nsigaret balance: ', sigaret_balance)
'''

'''
balance = 0
terminal = int(input('money: '))
balance += terminal
print('Balance: ', balance, '$')
shop = int(input('shop: '))
succses = balance >= shop
print('end balance', balance, 'your paymnet will done', succses)
'''

'''
num= (int(input('gri arajin tivy: ')))
num2= (int(input('gri toksi tivy: ')))
tokos = num * (num2/100)
patasxan = tokos+num
print(tokos)
print(patasxan)
'''


num= (int(input('gri arajin tivy: ')))
num1= (int(input('gri erkord tivy: ')))
num2= (int(input('gri errord tivy: ')))
tokos = (int(input('tokosi tivy: ')))

sum = num+num1+ num2
tokos = sum * (sum/100)
inqnarjek = sum-tokos
print(tokos, inqnarjek)






