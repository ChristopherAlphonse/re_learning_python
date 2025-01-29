# Given a list of strings strs, containing the strings "red", "green" and "blue", partition the list so that the red come before green, which come before blue.

# Constraints

# n ≤ 100, 000 where n is the length of strs.

# This should be done in \mathcal{O}(n)O(n) time.

# Bonus: Can you do it in \mathcal{O}(1)O(1) space? That is, can you do it by only rearranging the list (i.e. without creating any new strings)?
strs = ["green", "blue", "red", "red"]
# expected ["red", "red", "green", "blue"]


def partitionList(strs):

    middle = len(strs) // 2
    l = strs[:middle]
    r = strs[middle:]

    return r+l


print(partitionList(strs))
