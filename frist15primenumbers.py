def main():
    print('this code print the first fifteen number is in a given range')
    num = 15
    print_prime_number(num)

def print_prime_number(num):   
    n = 2
    count = 1
    while count <= num:
        if is_prime(n) is True:
            print(f'{n} is a prime number')
            count=sum((count,1))
        n = sum((n,1))

def is_prime(num):
    if count_of_factors(num) == 2:
        return True
    return False

def count_of_factors(num):
    count = 0
    for i in range(1, num+1):
        if num % i == 0:
            count +=1
    return count

main()             




