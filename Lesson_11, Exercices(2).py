'''
for i in range(1, 181):
    if i % 12 ==0 and i%15==0:
        print(i)
        break
'''

'''
import time
number_one = int(input('number one: '))
number_two = int(input('number two: '))

start = time.time()
if number_one > number_two:
    big =number_one
else:
    big = number_two

end = number_two* number_two+1
for i in range(big, end, big):
    #print(i)
    if i % number_one ==0 and i% number_two==0:
        print(i)
        break

ends = time.time()
print(ends-start)
'''

'''
odd = 0
even =0
for i in range(1,100 +1):
    if i %2==0:
        even==1
    else:
        odd ==1
print('odd: ',odd, 'even: 'even)

'''

'''
x,y =0,1
while x < 40:
    print(x)
    x,y = y, x + y
'''

'''
word = 'python 3.9'
letter =0
number =0
for i in word:
    if i.isalpha():
        letter +=1
    elif i.isdigit():
        number +=1

print(letter, number)
'''

'''
num = input('gri tiv: ')

count =0
for i in num:
    count +=int(i)
print(count)
'''

'''
num = int(input('gri tiv: '))
count =1
for i in range(1, num+1):
    count *= i
print(count)
'''


'''
number_one = int(input('number one: '))
number_two = int(input('number two: '))

if number_one < number_two:
    small = number_one
else:
    small = number_two
for i in range(small, 0, -1):
    if  number_one % i==0 and number_two %i ==0:
        print(i)
'''

number_one = int(input('number one: '))
number_two = int(input('number two: '))
if number_one < number_two:
    small = number_one
else:
    small = number_two
for i in range(2, small +1):
    if  number_one % i==0 and number_two %i ==0:
        print(i)
        break
else:
    print(i)


