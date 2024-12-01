#linear search is only used for unordered list
people = ['Favour', 'Elvis', 'Cate', 'Ernest', 'Linet']
find = 'Linet'
found = False
counter = 1

for person in people:
    if person == find:
        found = True
        print('Found at position', counter)
    else:
        counter = counter + 1

if not found:
    print('Person not found.')