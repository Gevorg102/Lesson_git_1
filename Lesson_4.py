print()



# 1. Դուք ունեք մեկ մուտք, որտեղ դուք գրում եք համարը (Celsius), եւ ձեր ծրագիրը կասի, քանի Fahrenheit- է Ձեր Celsius աստիճանը.
'''
cels = int(input('gri celsus@: '))
far= 32 + cels * 1.8
print('farenheit@: ', far)
'''

# 2. Հակարակը Fahrenheit-ը դարձրեք Celsius
'''
far = float(input('gri farenheit: '))
cels = (far-32)/1.8
print('celsus: ', cels)
'''

# 3.Ստեղծեք ծրագիր ստուգելու համար, թե արդյոք Ձեր տրված տարը մեծատառով է
'''
tar = str(input('gri cankacac tar: '))
result = tar == tar.upper()
print(result)
'''

# 4. Greq tiv ev staceq te qani hat zuyq ev kent kstacwi ayd twic
'''
tiv = int(input('qani hat zuyg ev kent, gri tiv: '))
tiv_1= tiv // 2
tiv_2= tiv- tiv_1
print(tiv_1, tiv_2)
'''

# 5. Yntreq sharawzxi erkarutyun@ ev staceq 5 amboxch ptuyti erkarutyun@
'''
radius = float(input('hing ptuytic inchqan kkatari, gri sharavix@:  '))
Pi = 2.14
c = 2* Pi * radius
ptuyt= c*5
print(ptuyt)
'''

# 6. Գրեք ծրագիրը python-ում, որն ունի 2 մուտք (float կամ int), եւ նրանցից երկուսը պակաս են 90-ից, Ստուգեք, որ եռանկյունն ունի 90 աստիճանի անկյուն

'''
ank_1 = int(input('gri ankyun 1: '))
ank_2 = int(input('gri ankyun 2: '))

ank_3 = 180-ank_1-ank_2

print(ank_3)
'''

# tnayin grenq erku xndir angleren ev qcumenq opshi chat


# 7. Greq or ev staceq dra jam@, ropen, ev vayrkyan@
'''
day = int(input('gri or: '))
jam = day *24
rope = jam*60
second = rope * 60
print('day: ', day, 'jam: ', jam, 'jam: ', 'second: ', second)
'''


# 8.Gri tiv wor@ bajanwum e 400, ete ha petq e ta True, ete woch False
'''
num = int(input('gri tiv wor@ bajanwum e 400-i: '))
a= num % 400== 0
print(a)
'''

