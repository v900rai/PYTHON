num=int(input('enter a no'))
sum=0
for n in range(1, num):
    if num % n ==0:
        sum=sum+n
        if sum == num:
            print('no is perfect no')

        else:
                print('no is not perfect')

  
