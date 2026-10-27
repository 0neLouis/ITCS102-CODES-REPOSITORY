size = int(input(" Input desired size -->"))
for x in range(size, 20,):
    for y in range(x):
        print("*", end=" ")
    size *= 2
    print() 