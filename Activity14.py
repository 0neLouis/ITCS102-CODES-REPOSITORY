age = int(input("Input your age -->"))
is_employed = bool(input("Are you currently emplyed (True/False) -->"))
credit_score = int(input("Input your credit score-->"))
annual_income = float(input("Your annual income--?"))   
has_collateral = bool(input("Do you have collateral (True/False) -->"))

rate = 0.0
if age >= 21 and is_employed == True:
    print("You passed the baseline requirement")
    if credit_score >=750: #Tier1
     print("You have a high credit score")
     if annual_income >= 100000:
            rate = 4.5
            print("YOU HAVE A HIGH SALARY AND HIGH CREDIT SCORE! your credit score is" rate)
     else:
             rate = 5.0
            ("I'm sorry, you dont qualify")
    if credit_score <= 600 and credit_score < 700: #Tier2
        rate = 8.0
        if has_collateral == True:
            rate = (rate - 7.0%)
            print(rate - 7.0% )
        elif annual_income <= 400000:
            print(rate = 9.5%)
    if credit_score < 600: #Tier3
        print("REJECTED: credit score too low")
            
else:
    print("You are not qualified")