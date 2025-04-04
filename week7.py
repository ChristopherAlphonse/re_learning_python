# # Problem 1: Counting the Layers of a Sandwich
# # You're working at a deli, and need to count the layers of a sandwich to make sure you made the order correctly. Each layer is represented by a nested list. Given a list of lists sandwich where each list [] represents a sandwich layer, write a recursive function count_layers() that returns the total number of sandwich layers.

# # Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

# def count_layers(sandwich):
#     # base case
#     if len(sandwich) == 1:
#         return 1
#     return 1 + count_layers(sandwich[1])


# # Example Usage:

# sandwich1 = ["bread", ["lettuce", ["tomato", ["bread"]]]]
# sandwich2 = ["bread", ["cheese", ["ham", ["mustard", ["bread"]]]]]

# print(count_layers(sandwich1))
# print(count_layers(sandwich2))
# # Example Output:

# # 4
# # 5


# Problem 2: Reversing Deli Orders
# The deli counter is busy, and orders have piled up. To serve the last customer first, you need to reverse the order of the deli orders. Given a string orders where each individual order is separated by a single space, write a recursive function reverse_orders() that returns a new string with the orders reversed.

# Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.


# # function to reverse the orders in a list
# def reverse(input):
#     order = list(input)
#     print(order)
#     if len(order) == 1:
#         return order

#     return reverse(order[1:]) + order[0]


# def reverse_orders(orders):
#     # split the orders
#     order = orders.split()
#     return ' '.join(reverse(order))


# Example Usage:
# Example Output:

# def reverse_helper(words):
#     if len(words) == 0:  # Base case: no words left to process
#         return "
#     if len(words) == 1:  # Base case: only one word left
#         return words[0]
#     # Recursive case: reverse the rest and append the first word at the end
#     return reverse_helper(words[1:]) + " " + words[0]

# def reverse_orders(orders):
#     words = orders.split()  # Split the sentence into a list of words
#     return reverse_helper(words)  # Call the external helper function with the list of words


# def reverse_orders(orders):
#     if (orders.rindex('') == -1):
#         return []
#     first = orders[:orders.rindex('')]
#     second = orders[orders.rindex(''):]
#     return second + reverse_orders(first)


def reverse_orders(orders):

    if not orders:
        return []

    return [orders[-1]] + reverse_orders(orders[:-1])

    print(reverse_orders("Bagel Sandwich Coffee"))

    # Coffee Sandwich Bagel

    # other approach
