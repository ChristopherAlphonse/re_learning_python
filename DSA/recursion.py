def print_items(n):
    # base case

    if n == 0:
        return
    print("ul", n)
    print_items(n - 1)
    print("o l", n)


n = 3
print(print_items(n))
print("complete")
