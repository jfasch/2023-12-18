l = []

l.append(42)
l.append(1.234)
l.append(True)
l.extend([False])
l.extend(['abc', 'def'])
l.append([1, 1.0, 'eins'])
l.append((1, 1.0, 'eins'))
l.append(   {1, 1.0, 'eins'}    )
l.append(   {'one': 1, 'one point zero': 1.0, 'eins': 'eins'}    )

print(l)
