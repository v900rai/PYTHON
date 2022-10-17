base = int(input('enter a base'))
power = int(input('enter the ppower'))
res = 1
for _ in range (power):
    res = res*base
    print(f'{base} to the power of {power} = {res}')
    

