current_movies = {
    "The Grinch": "7:00PM",
    "Moana 2": "8:00PM",
    "Wicked": "9:00PM",
    "Red One": "10:00PM",
}

print("We're showing the following movies:")
for key in current_movies:
    print(key)

user_input = input("What movie would you like to see?\n")

showtime = current_movies.get(user_input)

if showtime == None:
    print("Please enter a movie from the list", key)
else:
    print(f"The showtime for {user_input} is {showtime}")
