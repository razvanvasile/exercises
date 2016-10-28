# Input: one integer
# Output: all prime numbers lower then that integer

import sys

def prime(number):
    if number < 2:
        return False
    is_prime = True
    for i in range(2, number):
        if number%i == 0:
            is_prime = False
    return is_prime

def lower_primes(number):
    if number < 2:
        return -1

    primes = list()
    for i in range(2, number+1):
        print(i, number)
        if prime(i):
            primes.append(i)
    return primes


if __name__ == '__main__':
    number = int(float(sys.argv[1]))
    primes = lower_primes(number)
