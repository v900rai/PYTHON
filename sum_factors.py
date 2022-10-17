n=int(input('enter the number:'))
res=0
for div in range (1, n+1):
    if n % div == 0:
        res += div
        print(div)
print(f'Sum of {n} factors :{res} ')

