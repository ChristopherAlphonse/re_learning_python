contacts = {
    "number": 1,
    "student": [
        {"name": "John Doe", "email": "john@example.com"},
        {"name": "Jane Doe", "email": "janeD@example.com"},
        {"name": "Alice Smith", "email": "alice@example.com"},
        {"name": "Bob Brown", "email": "bob@example.com"},
        {"name": "Charlie Black", "email": "charlie@example.com"},
    ],
}

print("Student Email list \n")

for key in contacts["student"]:
    print(key["email"])
