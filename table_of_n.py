num = int(input('enter the number to get its table'))
mul = int(input('enter till wher u want the table '))

for n in range (1, mul + 1):
    print(f'{num} * {n} = {n * num}')