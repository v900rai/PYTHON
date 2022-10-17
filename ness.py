num1=int(input('enter the no'))
num2=int(input('enter the no'))
num3=int(input('enter the no'))
if num1==num2 or num2==num3 or num3==num1:
    print('2 or more  number are same , please diff num')
else:
    if num1>num2:
        if num1>num3:
            print(f'{num1}')
        else:
             print(f'{num3}')
    elif num2>num3:
        print(f'{num2}')
    else:
        print(f'{num3}')