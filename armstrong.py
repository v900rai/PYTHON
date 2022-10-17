def main():
    num = int(input('enter the number'))
    is_armstrong(num)

def is_armstrong(num):
    if num == armstrong_0p(num):
        print(f'{num} is an amstrong number')

    else:
        print(f'{num} is not an amstrong number') 

def armstrong_0p(num):
    count_of_digit = count_number_of_digit(num)
    res = 0
    while num :
        last_digit = num%10
        res = sum((res, pow (last_digit, count_of_digit))) 
        num = remove_last_digit(num)    
        return res

def count_number_of_digit(num):
    count = 0
    while num :
        num = remove_last_digit(num)
        count = sum((count, 1))
        return count
        
def remove_last_digit(num):
    return num // 10

main()            



