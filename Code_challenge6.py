ey = int(input(' Input desired number -->'))
num = 1
for x in range(ey):
    for y in range(x + 1):
        print(y, end=" ")
        num += 1
    print()