# Problem 1: Find Millenium Falcon Part
# Han Solo's ship, the Millenium Falcon, has broken down and he's searching for a specific replacement part.
# As a repair shop owner helping him out, write a function check_stock() that takes in a list inventory where
# each element is an integer ID of a part you stock in your shop, and an integer part_id representing the integer
# ID of the part Han Solo is looking for . Return True if the part_id is in inventory and False otherwise.

# Your solution must have O(log n) time complexity.


# def check_stock(inventory, part_id) -> bool:
#     # Assume that the list is sorted in increasing order
#     mid = len(inventory) // 2
#     if mid >= len(inventory):
#         return False

#     if inventory[mid] == part_id:
#         return True
#     elif (inventory[mid] > part_id):
#         return check_stock(inventory[0:mid], part_id)
#     else:
#         return check_stock(inventory[mid + 1:], part_id)


# print(check_stock([1, 2, 5, 12, 20], 20))
# print(check_stock([1, 2, 5, 12, 20], 100))
# print(check_stock([100], 100))
# print(check_stock([], 100))


# Problem 2: Find Millenium Falcon Part II
# If you implemented your check_stock() function from the previous problem iteratively, implement it recursively. If you implemented it recursively, implement it iteratively.


# def check_stock(inventory, part_id):
#     low = 0
#     high = len(inventory) - 1
#     while (low <= high):
#         mid = (low+high)//2
#         if (inventory[mid] == part_id):
#             return True
#         elif (inventory[mid] < part_id):
#             low = mid + 1
#         else:
#             high = mid - 1
#     return False


# # Example Usage:

# print(check_stock([1, 2, 5, 20, 12], 20))
# print(check_stock([1, 2, 5, 20, 12], 100))
# print(check_stock([100], 100))
# print(check_stock([], 100))
# # Example Ouput:

# # True
# # False

# Problem 3: Find First and Last Frequency Positions
# The Rebel Alliance has intercepted a crucial sequence of encrypted transmissions from the evil Empire.
# Each transmission is marked with a unique frequency code, represented as integers,
# and these codes are stored in a sorted array transmissions. As a skilled codebreaker for the Rebellion,
# write a function find_frequency_positions() that returns a tuple with the first and last indices of a
# specific frequency code target_code in transmissions. If target_code does not exist in transmissions, return (-1, -1).

# Your solution must have O(log n) time complexity.


# def find_frequency_positions(transmissions, target_code):
#     # result = (-1, -1)
#     first = -1
#     last = -1

#     high = len(transmissions)-1
#     low = 0

#     # find first part of frequency
#     while low <= high:
#         mid = (high + low)//2
#         if transmissions[mid] == target_code:
#             first = mid
#             high = mid - 1
#         if transmissions[mid] < target_code:
#             low = mid + 1
#         # if transmissions[mid] < target_code:
#         else:
#             high = mid - 1

#     # find last part of frequency
#     last = -1
#     high = len(transmissions)-1
#     low = 0
#     while low <= high:
#         mid = (high + low)//2
#         if transmissions[mid] == target_code:
#             last = mid
#             low = mid + 1
#         if transmissions[mid] < target_code:
#             low = mid + 1
#         # if transmissions[mid] > target_code:
#         else:
#             high = mid - 1

#     return (first, last)


#     # Example Usage:
# print(find_frequency_positions([5, 7, 7, 8, 8, 10], 8))
# print(find_frequency_positions([5, 7, 7, 8, 8, 10], 6))
# print(find_frequency_positions([], 0))

# [5, 7, 7, 7, 7, 7, 8, 8, 8, 8, 10], 8)
#           ^


# Example Output:

# (3, 4)
# (-1, -1)
# (-1, -1)
\
'''
Problem 3: Sqrt(x)
Given a non-negative integer x, use binary search to return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

You may not use any built-in exponent function or operator. You may not use any external libraries like math.

For example, do not use pow(x, 0.5) or x ** 0.5.
Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.
'''


from cmath import sqrt


def my_sqrt(x) -> int:
    if x < 2:
        return x

    left, right = 0, x
    while left <= right:
        mid = (left + right) // 2
        square = mid * mid
        if square == x:
            return mid
        elif square < x:
            left = mid + 1
        else:
            right = mid - 1
    return right


print(my_sqrt(4))
print(my_sqrt(8))
print(my_sqrt(9))
print(my_sqrt(16))
print(my_sqrt(12))
print(my_sqrt((2147395599)))
print(sqrt(2147395599))

# Example Output:
# 2
# 4
# Example 2 Explanation: The square root of 8 is 2.82842..., and since we round it down
# to the nearest integer, the answer is 2.
