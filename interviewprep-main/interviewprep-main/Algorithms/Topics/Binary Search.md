# Binary Search

## Explanation

# Binary search only works on a pre-sorted list

# Example

# [2, 3, 5, 8, 10, 15, 22, 23]

# ^ ^ ^

# low mid high

# - If the item at the midpoint is correct, return it

# - If the item at the midpoint is greater than the target, move `high` below mid

# [2, 3, 5, 8, 10, 15, 22, 23]

# ^ ^

# low high

# - If the item at the midpoint is lesser than the target, move `low` above mid

# [2, 3, 5, 8, 10, 15, 22, 23]

# ^ ^

# low high

# - Keep going until the guess is found. This can be done both recursively and iteratively

## < or <=?

# - If returning from inside the loop, use `low <= high`

# - If reducing the search space and returning after the loop, use `low < high` and return `low` at the end

## Implementation

# Iterative Binary Search

def binary_search(array: list[int], target: int) -> int:
low, high = 0, len(array) - 1

    while low <= high:
        mid = low + (high - low) // 2
        guess = array[mid]

        if guess == target:
            return mid
        elif guess < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1  # Target not found

# Recursive Binary Search

def binary_search_recursive(array: list[int], target: int, low: int, high: int) -> int:
if low > high:
return -1 # Target not found

    mid = low + (high - low) // 2
    guess = array[mid]

    if guess == target:
        return mid
    elif guess < target:
        return binary_search_recursive(array, target, mid + 1, high)
    else:
        return binary_search_recursive(array, target, low, mid - 1)

### Big O

Runs in $O(log \cdot n)$ time.
