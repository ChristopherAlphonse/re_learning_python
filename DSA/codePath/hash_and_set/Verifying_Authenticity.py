# Your art gallery has just been shipped a new collection of numbered art pieces, and you need to verify their authenticity. The collection is considered "authentic" if it is a permutation of an array base[n].

# The base[n] array is defined as [1, 2, ..., n - 1, n, n], meaning it is an array of length n + 1 containing the integers from 1 to n - 1 exactly once, and the integer n twice. For example, base[1] is [1, 1] and base[3] is [1, 2, 3, 3].

# Write a function is_authentic_collection that accepts an array of integers art_pieces and returns True if the given array is an authentic array, and otherwise returns False.

# Note: A permutation of integers represents an arrangement of these numbers. For example[3, 2, 1] and [2, 1, 3] are both permutations of the series of numbers 1, 2, and 3.


# permutation: a way, especially one of several possible variations, in which a set or number of things can be ordered or arranged.


# The collection is considered "authentic" if it is a permutation of an array base[n]
# no dups but n -4,
# highest int needs to be there twice

import unittest

# find max value in art pieces
# check if the length of art pieces is in n + 1
# count freq  of each art piece
# auth case for  base[n]
# each num1 to n - 1 exactly once, and the integer n twice
# return boolean


def is_authentic_collection(art_pieces):
    max_value = max(art_pieces)

    if len(art_pieces) != max_value + 1:
        return False
    res = {}
    for art in art_pieces:
        if art in res:
            art_pieces[art] += 1
        else:
            art_pieces[art] = 1

    for i in range(1, len(art_pieces)):
        if res.get(i, 0) != 1:
            return False

    return res.get(max_value, 0) == 2


class Test(unittest.TestCase):

    def test1(self):
        collection1 = [2, 1, 3]
        return self.assertFalse(is_authentic_collection(collection1), False)

    def test2(self):
        collection2 = [1, 3, 3, 2]
        return self.assertTrue(is_authentic_collection(collection2), True)

    def test3(self):
        collection3 = [1, 1]
        return self.assertTrue(is_authentic_collection(collection3), True)


if __name__ == "__main__":
    unittest.main()
