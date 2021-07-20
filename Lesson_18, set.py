'''
s = {'Narek', 'Gevorg', 'Narek', 78, 50} #set
for i in s:
    if i =='Gevorg':
        print(i)
        '''
'''
s = {0, 1, 99}
s.add(8)

z = {4, 31, 3, 2, 88}
s.update(z)
print(s)

c = set('g ev')
print(c)

'''

'''
s = {1, 12, 34}
# s.discard(123) ## sxal chi ta i tarberutyun remove-i
if 123 in s:
    s.remove(123)
else:
    print(s)
'''

'''
set1 = {'a', 'b', 'c'}
set2 = {1, 3, 'b', 'z'}
set3 = set1.union(set2)  #miacnum e, i tarberutyun update-i petq evs mi popoxakan
print(set3)
'''

'''
set1 = {'a',  'c', 15}
set2 = {1, 3, 'b', 'z'}
res = set1.isdisjoint(set2) #isdisjoint__ ete nshvac seterum gone 1 hat nuyn elementy ka kta 'False'hakarak depqum True
print(res)
'''
'''
set1 = {15, 12, 81}
set2 = {15,  731, 3}

res = set1.intersection(set2)  #cuyc e talis te woronq en krknwum  ete chka kta 'set()'
res1 =set2.pop() #amenpoqrn e cuyc twel
print(res1)
print(res)
'''

# ete elementy krknwum e, jnji
s = [1, 1, 45, 4, 7, 3, 98, 45]

'''
res = [i for i in s if s.count(i) ==1]
print(res)
print(set(res))
'''
'''
res = []
for i in s:
    if s.count(i) ==1:
        res.append(i)

print(set(res))
'''

# unenq miat set naxawrjin amenamec tivy inchqanow e poqr 100-ic

# s ={48, 2, 3, 15, 34}
'''
num =sorted(s)
a = num[-2]
b =100
print(b-a)
'''

s ={48, 2, 3, 15, 34}
a = list(s)
b =0

for i in a:
    if a[i] > b:
        b = a[i]
c = 0
for i in a:
    if a[i] > b and  a[i]!=b:
        b = a[i]

print(c)



