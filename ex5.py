# Used for unordered list

students = ['Enest', 'Jane', 'Favour', 'Elvis', 'Abel', 'David']
find = 'Favour'
found = False #found variable to keep track of whether we found favour or not
counter = 1

for student in students:
    if student == find:
        found = True
        print(f"found at position {counter}")

    else:
        counter = counter + 1

if not found:
    print("Student not found")            