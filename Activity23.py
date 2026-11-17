shonen = []
korean = []
isekai = []
adventure = []
fantasy = []

while True:
    ans = input("Do you watch any anime? --> yes/no").lower()
    
    if ans == "yes":
        print("What kind o Anime do you watch?")
    print("1 shonen \n2 korean \n3 isekai \n4 adventure \n5 fantasy")
    
    choice = int(input(" Input --> "))
    if choice == 1:
        print("SHONEN")
    title = input(" Please input the title of the anime -->")
    shonen.append(title)
    print(shonen)
    con = input("Do you wish to continue? yes/no ")    
    if con == yes:
        continue
    else:
        break
else: 
    print("Invalid choice")