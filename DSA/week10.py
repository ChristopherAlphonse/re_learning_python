"""
Problem 1: There and Back
As a flight coordinator for CodePath airlines, you have a 0-indexed adjacency list flights with n nodes where each node represents the ID of a different destination and flights[i] is an integer array indicating that there is a flight from destination i to each destination in flights[i]. Write a function bidirectional_flights() that returns True if for any flight from a destination i to a destination j there also exists a flight from destination j to destination i. Return False otherwise.

    """


def bidirectional_flights(flights) -> bool:
    for row in range(len(flights)):
        for col in range(len(flights[row])):
            current_flight = flights[row][col]
            if row not in flights[current_flight]:
                return False

    return True


flights1 = [[1, 2],
            [0],
            [0, 3],
            [2]]

# 0 --> 1
# |
# 2 <-- 3

flights2 = [
    [1, 2],
    [],
    [0],
    [2]
]

# print(bidirectional_flights(flights1))
# print(bidirectional_flights(flights2))

"""
    Problem 2: Find Center of Airport
You are a pilot navigating a new airport and have a map of the airport represented as an undirected star graph with n nodes where each node represents a terminal in the airport labeled from 1 to n. You want to find the center terminal in the airport where the pilots' lounge is located.

Given a 2D integer array terminals where each terminal[i] = [u, v] indicates that there is a path (edge) between terminal u and v, return the center of the given airport.

A star graph is a graph where there is one center node and exactly n-1 edges connecting the center node ot every other node.
    """


def find_center(terminals):
    a, b = terminals[0]
    c, d = terminals[1]
    if a in (c, d):
        return a
    return b


terminals1 = [[1, 2],
              [2, 3],
              [4, 2]]

terminal3 = [
    [3, 3],
    [3, 6],
    []
]
# terminals2 = [[1, 2], [5, 1], [1, 3], [1, 4]]

print(find_center(terminals1))
# print(find_center(terminals2))
