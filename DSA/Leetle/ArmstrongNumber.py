# time to solve 4 mins

def isArmstrong(num):
    num_str = str(num)
    num_digit = len(num_str)

    total = 0
    for digits in num_str:
        total += int(digits) ** num_digit
    return total == num


print(isArmstrong(153))  # True
print(isArmstrong(1634))  # True
print(isArmstrong(123))  # False
