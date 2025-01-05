# Write a program that takes a date as input and outputs the date's season in the northern hemisphere. The input is a string to represent the month and an int to represent the day.

# Ex: If the input is:

# April
# 11
# the output is:

# Spring
# In addition, check if the string and int are valid (an actual month and day).

# Ex: If the input is:

# Blue
# 65
# the output is:

# Invalid
# The dates for each season in the northern hemisphere are:
# Spring: March 20 - June 20
# Summer: June 21 - September 21
# Autumn: September 22 - December 20
# Winter: December 21 - March 19

# TODO: Improve code

input_month = input()
input_day = int(input())

months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

if input_month not in months or input_day < 1 or input_day > 31:
    print("Invalid")
else:
    # Winter: December 21 - March 19
    if input_month in ["December", "January", "February", "March"]:
        if (input_month == "December" and input_day >= 21) or (input_month == "March" and input_day <= 19) or input_month == "January" or input_month == "February":
            print("Winter")
        else:
            print("Invalid")
    # Spring: March 20 - June 20
    elif input_month in ["March", "April", "May", "June"]:
        if input_month == "June" and input_day <= 21:
            print("Summer")
        elif (input_month == "March" and input_day >= 20) or (input_month == "June" and input_day <= 20) or input_month in ["April", "May"]:
            print("Spring")
        else:
            print("Invalid")
    # Autumn: September 22 - December 20
    elif input_month in ["September", "October", "November", "December"]:
        if (input_month == "September" and input_day >= 22 and input_day < 31) or (input_month == "December" and input_day <= 20) or input_month in ["October", "November"]:
            print("Autumn")
        else:
            print("Invalid")
     # Summer: June 21 - September 21
    elif input_month in ["June", "July", "August", "September"]:
        if (input_month == "June" and input_day >= 21) or (input_month == "September" and input_day <= 21) or input_month in ["July", "August"]:
            print("Summer")
