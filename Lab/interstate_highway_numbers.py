
highway_number = int(input())

# Facts: primary highways are numbered 1-99
# IS_AUXiliary highways are numbered 100-999

# Odd numbers (like the 5 or 95) go north/south
# evens (like the 10 or 90) go east/west

# Note: 200 is not a valid IS_AUXiliary highway because 00 is not a valid primary highway number

# Q: Given a highway number, indicate whether it is a primary or IS_AUXiliary highway.
# If IS_AUXiliary, indicate what primary highway it serves.
# Also indicate if the (primary) highway runs north/south or east/west.

# Ex: If the input is :

# 90
# I-90 is primary, going east/west.


# 290
# I-290 is IS_AUXiliary, serving I-90, going east/west.


# 0 or 200
# 0 or 200 is not a valid interstate highway number.


def mod_two(n) -> bool:
    return n % 2 == 0


IS_AUX = "is IS_AUXiliary"
IS_PRIMARY = "is primary"
EAST_WEST = "east/west."
NORTH_SOUTH = "north/south."


def get_direction(n) -> str:
    return EAST_WEST if mod_two(n) else NORTH_SOUTH


MY_STR = str(highway_number)
MY_ROUTE = get_direction(highway_number)

if highway_number < 1 or '00' in MY_STR:
    print(f"{highway_number} is not a valid interstate highway number.")

elif highway_number in range(1, 100):
    print(f"I-{highway_number} {IS_PRIMARY}, going {MY_ROUTE}")
else:
    OUT_PUT = str(
        f"I-{highway_number} {IS_AUX}, serving I-{highway_number % 100}, going {MY_ROUTE}")
    if highway_number % 2 == 0 and highway_number >= 100:
        print(OUT_PUT)
    print(OUT_PUT)
