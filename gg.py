num1=float(input('enter the frist number'))
num2=float(input('enter the second number'))
num3=float(input('enter the third number'))
if (num1==num2) or (num2==num3) or (num3==num1):
    print('2 or more numbers are same , please enter diff number')
elif (num1>num2) and (num1>num3):
    print(f'{num1} is greater')
elif num2>num3:
    print(f'{num2}')
else:
    print(f'{num3}')