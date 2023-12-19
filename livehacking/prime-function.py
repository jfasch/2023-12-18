import numbertools
import sys

if len(sys.argv) == 1:
    number = int(input('Bitte gib eine natuerliche Zahl ein: '))
else:
    number = int(sys.argv[1])

if numbertools.is_prime(number):
    print('prime')
else:
    print('not prime')
