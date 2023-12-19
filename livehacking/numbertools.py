import sys
import time

def is_even(number):
    return number%2 == 0

def is_prime(number):
    if number == 1:
        return False

    for divisor_candidate in range(2, number):
        if number % divisor_candidate == 0:
            return False
    return True

if __name__ == '__main__':
    if len(sys.argv) == 1:
        number = int(input('Bitte gib eine natuerliche Zahl ein: '))
    else:
        number = int(sys.argv[1])

    if is_prime(number):
        print('prime')
    else:
        print('not prime')

