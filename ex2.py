numbers = [4, 2, 46, 8, 1, 13, 6, 58, 10]
find = 6
found = False
counter = 1

for number in numbers:
    if number == find:
        found = True
        print('Found at position', counter)
    else:
        counter = counter + 1

if not found:
    print('Number not found')            


