import sys, re

rex_empty = re.compile(r'^\s*($|#.*$)')

f = open(sys.argv[1], encoding='ascii')
for line in f:
    match = rex_empty.search(line)
    if match is not None:
        continue
    
    # stripped = line.strip()

    # if stripped == '':
    #     continue
    # if stripped == '#':
    #     continue
    print(line, end='')
