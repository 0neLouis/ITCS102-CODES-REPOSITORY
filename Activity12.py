import getpass

#log in
username = 'avisala'
password = 'eshma'

u = input("Type your username -->")
p = getpass.getpass("Type your password -->")

u 

if username == u and p == password :
  print("Access granted!")
else:
  print("Access denied")
