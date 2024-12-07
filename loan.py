money_owed = float(input("How much money do you owe, in dollars? $"))
apr= float(input("What is your current interest rate %"))
payment=float(input("What will you pay each months? $"))
months=(int(input("How many months will you pay - 12, 24, 36 or 72? \n")))

monthly_rate = (apr/100)/12
for i in range(months):
    interest_charge = money_owed * monthly_rate
    money_owed = money_owed+ interest_charge
    if(money_owed -payment < 0):
        print("The last payment", round(money_owed, 2))
        print("You paid off the loan in", i+1, "months")
        break

    money_owed = money_owed- payment

print(f"Paid ${round(payment, 2)} of which ${round(interest_charge, 2)} was interest")
print( "Now I owe $", round(money_owed, 2))
