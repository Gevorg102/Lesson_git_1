print()

# poxi string@ dictinory

'''
s = 'a,2, b,5, c,8, a,4, e,11, a,5'.split(',')

c = {}
for i in range(0, len(s), 2):
    if s[i] in c:
        c[s[i]] = int(s[i+1]) + c[s[i]]
    else: 
        c[s[i]] = int(s[i+1])
print(c)
'''

# darcru string@ dictinory ev icnhqan ka tar@ aysqan value-um qanaky gri
'''
word = 'exercices'
# res ={}
# for i in word:
#     res[i] = word.count(i)

res = {i: word.count(i) for i in word}
print(res)
'''

old_list = [{'key':1},{'key':'value1'},{'key':'value1'}, {}, {},{}, {'key':'value1'}, {'key2':'value2'}, {'key':'value1'},{'key':'value1'}]
'''
for i in old_list:
    if old_list.count(i) >1:
        old_list.remove(i)

print(old_list)
'''

count =0
for i in range(len(old_list)):
    if old_list.count(old_list[count]) > 1:
        old_list.remove(old_list[count])
        
    else:
        count+=1
print(old_list)


#milionater tnayni@ petqa harcer gres tarberaknerow 5 harc (value key-ov) 