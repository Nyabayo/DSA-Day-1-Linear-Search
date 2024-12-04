numbers = [4, 2, 46, 1, 13, 6, 58, 10]
find = 4
found = False   #found variable will keep track whether we found 6 or not.
counter = 1

for number in numbers: #number is the value and numbers is the list
    if number == find:
        found = True
        print(f"found at position {counter}")
    else:
        counter = counter + 1

if not found:
    print("number not found")         