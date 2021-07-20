print()


'''
thisdict = {'name': 'Gevorg', 'year': 1994}
print(thisdict)
'''


'''
res = 0
c =[]
while True:
    students = {res: {'Name': None, 'Email': None, 'Phone': None}}

    

    user = input('name: ')
    email = input('email: ')
    phone = input('phone: ')
    students[res]['Name'] = user
    students[res]['Email'] = email
    students[res]['Phone'] = phone
    print(students)
    c.append(students)
    res+=1

    if res ==3:
        break
print(c)
'''


'''
thisdict = {'name': 'Saqo', 'year': 1994}
print(len(thisdict))
'''

'''
thisdict = {'Manvel': (18, 45), 'Saqo': [45, 102], 'Mariam': 21, 'Anna': 16, 'Anahit': 25,}
print(thisdict)
'''

'''
thisdict = dict(brand = 'ford', model = 'mustang', year = 1970)
print(thisdict)
'''

'''
students = {'name': 'Artur', 'email': 'art@mail.ru', 'age': 18}
for test in students.values():
    print(test)
for test in students.keys():
    print(test)
for key, value in students.items():
    print(key, value)
'''

'''
thisdict = {'name': 'Aram', 'year': 1994}
del thisdict['year']
print(thisdict)
'''

'''
students = {'Aram': 4, 'Gevorg': 2, 'Narek': 5}
key = None
value = None
for key in students:
    if students[key] ==5:
        print(key)
'''


'''
students = {'Aram': 4, 'Gevorg': 2, 'Narek': 5}
x = students.popitem()
print(x)
print(students)
'''

'''
students = {'Aram': 4, 'Gevorg': 2, 'Narek': 5}
stud =0
gnah =0
for value in students.values():
    stud +=1
    gnah += value
print(gnah/stud)
'''

students = {'Aram': 4, 'Gevorg': 2, 'Narek': 5}
gnah =0
name = ''
for i in students:
    if students[i] > gnah:
        gnah = students[i]
        name = i
      

gnah_1 =0

for i in students:
    if students[i] > gnah_1 and students[i]!=gnah:
        gnah_1 = students[i]
        name = i
      
print(gnah_1)

'''
for i in students:
    if students[i] > gnah:
        gnah = students[i]
        name = i     
    
print(gnah, name)
'''

# for i in students:
#     if students[i] == gnah:
#         print(i)

car = {'brand':48}
print(car.append('name'))