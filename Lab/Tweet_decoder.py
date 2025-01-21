# # The following program decodes a few common abbreviations in online communication such as messages in Twitter ("tweets") or email, and provides the corresponding English phrase.
# # tweet = input('Enter abbreviation from tweet:\n')

# # if tweet == 'LOL':
# #     print('LOL = laughing out loud')
# # elif tweet == 'BFN':
# #     print('BFN = bye for now')
# # elif tweet == 'FTW':
# #     print('FTW = for the win')
# # elif tweet == 'IRL':
# #     print('IRL = in real life')
# # else:
# #     print("Sorry, don't know that one")


# # Create different versions of the program that:

# # Expand the number of abbreviations that can be decoded. Add support for abbreviations you commonly use or search the internet for some.
# # Allow the user to enter a complete tweet (160 characters or less) as a single line of text. Search the resulting string for abbreviations and print a list of each abbreviation along with its decoded meaning.

# import requests
# abbreviations = {
#     'LOL': 'Laugh Out Loud',
#     'BFN': 'Bye For Now',
#     'FTW': 'For The Win',
#     'IRL': 'In Real Life',
#     'YOLO': 'You Only Live Once',
#     'BRB': 'Be Right Back',
#     'SMH': 'Shaking My Head',
#     'TMI': 'Too Much Information',
#     'IDK': 'I Don\'t Know',
#     'DM': 'Direct Message',
#     'TBH': 'To Be Honest',
#     'BFF': 'Best Friends Forever'
# }

# search = input('Enter word to be decoded: ').upper()
# if len(search) < 1 or len(search) >= 160:
#     print("Invalid . search mst be 160 characters or less must be in the range of 1-160.")
# elif search in abbreviations:
#     print(f"{abbreviations[search]}")
# else:
#     print("Word not found!")


# Constants
BASE_URL = "https://hackdiversity.xyz/api"
SESSION_ENDPOINT = "/start-session"
ROUTES_ENDPOINT = "/navigation/routes"
SORTED_ROUTES_ENDPOINT = "/navigation/sorted_routes"
TEST_MOCK_ENDPOINT = "/test/mockRoutes"
TEST_SUBMIT_ENDPOINT = "/test/submit-sorted-routes"

# Start Session


def start_session(first_name, last_name):
    response = requests.post(
        f"{BASE_URL}{SESSION_ENDPOINT}",
        json={"firstName": first_name, "lastName": last_name}
    )
    response.raise_for_status()
    return response.json().get("session_id")

# Fetch Routes


def fetch_routes(session_id, endpoint):
    headers = {"Authorization": f"Bearer {session_id}"}
    response = requests.get(f"{BASE_URL}{endpoint}", headers=headers)
    response.raise_for_status()
    return response.json()

# Filter Accessible Routes


def filter_accessible_routes(routes):
    return [route for route in routes if route.get("accessible")]

# Sort Routes by Distance


def sort_routes_by_distance(routes):
    for i in range(len(routes)):
        for j in range(0, len(routes) - i - 1):
            if routes[j]["distance"] > routes[j + 1]["distance"]:
                routes[j], routes[j + 1] = routes[j + 1], routes[j]
    return routes

# Submit Routes


def submit_routes(session_id, endpoint, sorted_routes):
    headers = {"Authorization": f"Bearer {session_id}"}
    response = requests.post(
        f"{BASE_URL}{endpoint}", json=sorted_routes, headers=headers)
    response.raise_for_status()
    return response.json()

# Main Program


def main():
    # Start Session
    session_id = start_session("Christopher", "Alphonse")

    # Retrieve Routes
    routes = fetch_routes(session_id, ROUTES_ENDPOINT)

    # Filter and Sort
    accessible_routes = filter_accessible_routes(routes)
    sorted_routes = sort_routes_by_distance(accessible_routes)

    # Submit Sorted Routes
    result = submit_routes(session_id, SORTED_ROUTES_ENDPOINT, sorted_routes)
    print("Submission Result:", result)


if __name__ == "__main__":
    main()
