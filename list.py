expenses = []

while True:
    user_expense = float(input("Enter an expense: \n"))
    expenses.append(user_expense)
    if user_expense == -1:
        break
    else:
        continue

print("Total expenses: ", sum(expenses))
