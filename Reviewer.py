age = int(input("Input your age -->"))
monthly_revenue = int(input("Input your monthly revenue --=>"))
credit_score = int(input("input ypur credit score "))
years_in_business = float(input("Input years in business -->"))
has_defaults = bool(input("Do you have previous records of bankruptcy? --?"))
collateral_name = str(input("Input collateral name -->"))
collateral_value = int(input("Input collateral value -->"))
                           
#baseline requirements

if age >= 21 and years_in_business >= 2.0 and has_defaults == False:
    print("you passed the baseline requirements!")
    if credit_score >= 720:#tier1
        max = 3 * monthly_revenue
        print("You have a high credit score")
        if monthly_revenue >= 50000:
            rate = 1.5
            fee = max * 0.015
            print("You have a high monthly revenue! You are qualified with a rate of", rate)
            print("your basefee is set to", fee)
            
#colloateral
            if  collateral_value >= max:
                print("Your collateral", collateral_name, "with a value of", collateral_value, "is accepted")
            else:
                print("Insuffiecient value of collateral")
#supercgarge
                surge = max * fee
                if max % 500 != 0:
                    print("You have an additional charge!")
                    surge += 250
                    print("updated base fee is", fee)
            

            if credit_score <= 620 and credit_score <=720:#Tier 2
                max = 1.5 * monthly_revenue
                print("you have an average credit score.")
                if years_in_business >= 5.0:
                    rate = 2.0
                    #supercharge
                    surge = max * fee
                    if max % 500 != 0:
                        print("You have an additional charge!")
                        surge += 250
                        print("updated base fee is", fee)
            
                    print(" You are qualified with a rate of", rate)
                elif credit_score < 620: #Tier3
                    print(" Rejected! credit score too low")
                    
                else:
                    rate = 3.5
                    print(" You are qualified with a rate of", rate)
                                        
                    
            
        else:
            rate = 2.5
            fee = max * 0.015
            print("You are qualified with a rate of", rate)
            print("your bas efee is set to", fee)


else:
    print("You are not eligible")