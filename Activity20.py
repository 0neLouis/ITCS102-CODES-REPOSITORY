u = "JuanONE1"
p = "111"

is_login = False

while is_login == False:
    
    user = input("Pleas einput username Id -->")
    pword = input("Please input password -->")
    
    if user == u and pword ==  p:
        print (" LOGIN SUCCESFULLY ")
        is_login = True
    else:
        print(" LOGIN DENIED ")
        is_login = False