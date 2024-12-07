breakfast = ["coffee", "tea", "Bagel", "Eggs"]
lunch = ["Rice", "Turkey Sandwich", "BLT"]
dinner = ["Soup", "Salad", "Pasta", "Taco"]

# menu = [*breakfast, *lunch, *dinner]
# * is spread operator, it unpacks the list and combines them into one list
# ** is used for dictionaries aka objects
# print(menu)


# menus = [[breakfast], [lunch], [dinner]]
# print(menus[0][0][3])

menus = {"breakfast": breakfast, "lunch": lunch, "dinner": dinner}
# print(menus)

for key, value in menus.items():
    print(f"{key}:{value}")
