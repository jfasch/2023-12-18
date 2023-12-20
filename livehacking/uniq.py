def uniq(l):
    seen = set()
    for elem in l:
        if elem not in seen:
            seen.add(elem)
            yield elem

input_list = [2, 3, 1, 10, 3, 3, 1, 10, 5, 2]
output_list = uniq(input_list)

for element in output_list:
    print(element)
