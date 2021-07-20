print()
import random

point =0
c = random.choice('pu')
if c =='u':

    while True:
        while True:
            end =3
            if point >18:
                end = 21- point
            user = input(f'number betwen 1-{end} ')
            if user.isdigit():
                user = int(user)
                if 0 < user <=end:
                    break
                else:
                    print('please input number between 1 -', end, 'not', user)
            else:
                print('please input number', user)

        print(f'{point} + {user} = {point+ user}')
        point +=user
        if point ==21:
            print('win pc')
            break
        end_pc = 3

        if point > 18:
            end_pc = 21-point
        
        # pc = random.randint(1, end_pc)
        # if point > 16 and point <20:
        
        #     pc = 20-point
        pc = 4-point % 4
        print(f'{point} + {pc} = {point+ pc}')
        point +=pc
        

        if  point ==21:

            print('win user')
            break

else:
    print('pc')
    while True:
        
        
        if point %4!=0:
            
            pc = 4-point % 4
        else:
            pc = random.randint(1, 3)
        print(f'{point} + {pc} = {point+ pc}')
        point +=pc
    

        
                
        while True:
            end =3
            if point >18:
                end = 21- point
            user = input(f'number betwen 1-{end} ')
            if user.isdigit():
                user = int(user)
                if 0 < user <=end:
                    break
                else:
                    print('please input number between 1 -', end, 'not', user)
            else:
                print('please input number', user)

        print(f'{point} + {user} = {point+ user}')
        point +=user
        if point ==21:
            print('win pc')
            break
        end_pc = 3

        if point > 18:
            end_pc = 21-point
            
        
        
    