import sys
import time

number = int(input('Bitte gib eine natuerliche Zahl ein: '))

if number == 1:
    print('not prime')
    sys.exit()

for divisor_candidate in range(2, number):
    if number % divisor_candidate == 0:
        print('not prime')
        break
else:
    print('prime')
