#to find the given number is perfect are not
# sum of all proper factors is same as the original number
#ex: num= 6,proper factors are 1,2,3
# sum of proper factors = 6, org_num=6, therfore perfect number
def main():
    num = int(input('enter a number-->'))
    is_perfect(num)

def is_perfect(num):
    if perfect_op(num) == num:
        print(f'{num} is a perfect number') 
    else:
        print(f'{num} is a not perfect number') 

def perfect_op(num):
    res = 0
    for i in range(1, num):
        if (num%i == 0):
            res =res +i
    return res

main()
    


