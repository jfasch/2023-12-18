import timeit

code = '''
for n in range(3):
    pass
'''

print(timeit.timeit(code))
