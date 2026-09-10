#Code challenge3

name = input("Name of sender -->")
type = input("What kind of product? -->")

is_Fragile = bool(input(" is your Item fragile? -->"))
weight = float(input("How much does it weight -->"))
distance = float(input("How far is the shipping place? -->"))
is_Expresseed = bool(input("Is it by express? -->"))
is_International = bool(input(" is it overseas --?"))

a = ( weight * 2.50 )
b = ( distance * 0.15 )
base_cost =  ( a + b )

print( base_cost)


#international
 total = (base_cost * 1.40)

otal1 = (total + 50)

#expressed
total2 = (base_cost * 120)
total3 = (total2 + 25)

#oversized
total4 = (base_cost + 30)

if weight <= 2.0 and distance <= 100:
   print("free of charge")

elif is_fragile == true and expressed == true:
	print( total1 and total3)

 
else:
   print("Invalid")


