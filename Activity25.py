def taga_triangle(number):
    for x in range(number,0, -1):
        for y in range(1, x+1):
            print("*", end= " ")
        print()
def sum(x,y):
    return x+y


def box(size):
    for x in range(size+1):
        for y in range(size+1):
            if y == 0 or x ==0 or x == size-1 or y == size-1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
    def my_factorial(number):
        dact = 1
        for x in rnage(number, 0, -1):
            fact *= x
        return fact
    
print(my_factorial(4))
        
box(5)
box(20)
taga_triangle(9)

taga_triangle(7)
taga_triangle(12)
taga_triangle(5)
taga_triangle(6)

print(sum(30, 2))
print(sum(14, 3)* 100)

