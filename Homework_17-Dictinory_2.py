# 1. Gri cragir textum harevan elementenrin miavorelu hamar
'''
text = [48, 2, 18, 3, 748, 18, 0, 731]

res = []
for i in range(0, len(text), 2):
    res.append(text[i]+ text[i+1])
print(res)
'''

#milionater tnayni@ petqa harcer gres tarberaknerow 5 harc (value key-ov) 

import random


milion = {'harc_1': '1991', 
          'harc_2': '2008', 
          'harc_3': 'linus_torvalds', 
          'harc_4': '1949', 
          'harc_5': 'wochmibanow'}

mil = random.randint(0,len(milion)-1)


quest1 = input(f'erb haytnwec python-@: {milion[mil]}')
if quest1 == milion[mil]['harc_1']:
    print('Chishteq patasxanel')

quest2 = input('erb haytnwec github-@: '+milion[mil])
if quest2 == milion[mil]['harc_2']:
    print('Chishteq patasxanel')

quest3 = input('ow e linux mijuk@ stexcel:: '+milion[mil])
if quest3 == milion[mil]['harc_3']:
    print('Chishteq patasxanel')

quest4 = input('erb haytnwec assembler-@: '+milion[mil])
if quest4 == milion[mil]['harc_4']:
    print('Chishteq patasxanel')

quest5 = input('inchow e arawel Windows 11-@ 10-ic: '+milion[mil])
if quest5 == milion[mil]['harc_5']:
    print('Chishteq patasxanel')


