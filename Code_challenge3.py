#Code challenge3

name = input("Name of sender -->")
type = input("What kind of product? -->")
is_Fragile = bool(eval(input(" is your Item fragile? -->")))
weight = float(input("How much does it weight -->"))
distance = float(input("How far is the shipping place? -->"))
is_express = bool(eval(input("Is it by express? -->")))
is_international = bool(eval(input(" is it overseas --?")))



base_cost = (weight * 2.5) + (distance * .15)

if  weight <= 2 and distance <= 100 and is_express == False and is_international == False :
	print("Free Shipping!")
	Total = 0
	
elif is_international == True and is_express == True :
	print("Package is International is applied")
	Total = (base_cost * 1.4) + 50

elif is_express == True or (is_international == True and weight > 20) : 
	print("Package is Express or Heavy International is applied")
	Total = (base_cost * 1.2) + 25

elif weight > 30 or distance > 1000 : 
	print("Oversized is applied")
	Total = base_cost + 30
	
else :
	Total = base_cost
	print("Standard rate is applied")




print("--------------------------")
print("Name of the sender : ", name)
print("Type of Item : ", type)
print("Total Output  : PHP ", Total)
