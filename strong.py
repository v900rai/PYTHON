# write aprogram to find out if a given number is strong number or not
def main():
    num=int(input("Enter a number:"))  
    is_strong(num)
 

def is_strong(num):
    if num == strong_op(num):
        print("Given number is a strong number")  
    else:  
        print("Given number is not a strong number") 

def strong_op(num):
    res = 0
    while num :
       last_digit = num % 10
       res = sum((res,factorial(last_digit)))
       num = remove_last_digit(num)
    return res



def remove_last_digit(num):
    return num // 10
def factorial(num):
    fact = 1
    for i in range(num, 1, -1):
        fact *= i
    return fact

main()