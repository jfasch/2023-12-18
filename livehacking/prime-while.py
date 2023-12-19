import sys

number = int(input('Bitte gib eine natuerliche Zahl ein: '))

if number == 1:
    print('not prime')
    sys.exit()

divisor_candidate = 2
while divisor_candidate < number:
    if number % divisor_candidate == 0:
        print('not prime')
        break
    divisor_candidate += 1
else:
    print('prime')

# divisor_candidate = 2
# is_prime = True

# while is_prime:
#     rest = number % divisor_candidate
#     if rest == 0:
#         is_prime = False
#     if divisor_candidate == number - 1:
#         break
#     divisor_candidate += 1

# if is_prime:
#     print('prime')
# else:
#     print('not prime')
