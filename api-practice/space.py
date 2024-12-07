import requests

response = requests.get("http://api.open-notify.org/astros.json").json()

# print(response)

for person in response["people"]:
    print(person["name"])
