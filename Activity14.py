age = int(input("Input your age -->"))
is_empployed = eval(input("Are you currently employed? (True/False) --> "))
credit_score = int(input("Input your credit score -->"))
annual_income = int(input("Input your annual income -->"))
has_collateral = eval(input("Do you have collateral? (True/False) --> "))
rate = 0.0

if age >=21 and is_empployed:#tier1
    base_rate = 5.0
    print("You passed the baseline requirement.")
    if credit_score >= 700:
        print("You have a high credit score")
        if annual_income >= 100000:
            print("You are qualified for a loan with an interest rate of 4.5%") 
        else:
            print("You are qualified for a loan with an interest rate of 5%")
    elif credit_score >= 600 and credit_score < 750:
        print("You have a medium credit score")
        if has_collateral == True: #tier2
            print("you are qualified for a loan with an interest rate of 7%")
        if annual_income <=40000:
            print("You are qualified for a loan with an interest rate of 9.5%")

    else:#Tier3
        print("Rejected, Credit score too low")
else: 
    print("You don't meet the requirements, Try again next time")

            
            
