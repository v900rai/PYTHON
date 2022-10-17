def main():
    print('this code print all the prime is given range')
    num1= read('enter the lower limit-->')
    num2= read('enter the upper limit-->')
    print_prime_number(num1, num2)


def print_prime_number(num1, num2):
    for num in range(num1, num2):
        if is_prime(num) is True:
            print(f'{num} is prime number')


def is_prime(num):
    if count_of_factors(num) == 2:
        return True
    return False


def count_of_factors(num):
    count = 0
    for i in range(1, num+1):
        if num % i == 0:
            count+= 1
    return count


def read(msg):
    return int(input(msg))
main()
