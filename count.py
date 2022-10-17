num=int(input('enter the  number '))
count=0

for n in range (1, num+1):
    if num%n==0:
        count=count+1 
        print(f' no of factors for{num} is {count}-')