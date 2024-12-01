n = [4, 2, 46, 8, 1, 13, 6, 58, 10]
fi = 10
fo = False
co = 1

for i in n:
    if i == fi:
        fo = True
        print(f"found on position, {co}")
    else:
        co = co + 1
if not fo:
    print('No such number')       