import sys

arg = sys.argv[1]
arg = int(arg)

# translation_table = {
#     0: 'zero',
#     1: 'one',
#     2: 'two',
#     3: 'three',
#     4: 'four',
#     5: 'five',
#     6: 'six',
#     7: 'seven',
#     8: 'eight',
#     9: 'nine',
# }

translation_table = dict(
    zero=0,
    one=1,
    two=2,
    three=3,
    four=4,
    five=5,
    six=6,
    seven=7,
    eight=8,
    nine=9,
)

print(translation_table)

# translation = translation_table[arg]
# print(translation)
