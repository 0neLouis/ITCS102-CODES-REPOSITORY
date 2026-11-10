ok = 5

for a in range(ok):
    for b in range(ok - a - 1):
        print(" ", end=" ")
        
        for c in range(ok):
            if a == 0 or a == ok-1 or c == 0 or c == ok-1:
                print("*", end=" ")
            else:
                print(" ", end= " ")
        print()  