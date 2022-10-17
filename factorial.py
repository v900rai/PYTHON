num=int(input('enter a  numaber'))
factorial= 1
if num <0:
    print('factorialdoes not exist for the nagative number')

elif num==0:
          print(f'(the factorial of 0 1)')
        
else: 
    for i in range (1,num+1):
        factorial=factorial*i

print(f'the factorial of {num} is {factorial}')