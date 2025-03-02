# find len of longest balance sub sequence
# the difference must exctaly  1

# count freq for each art pieces
# iterate through
# increase the count if found
# max len variable
# iterate through the dictionary to find unique pairs that have a difference of 1
import unittest


def find_balanced_subsequence(art_pieces):
    art_count = {}

    for art in art_pieces:
        if art in art_count:
            art_count[art] += 1
        else:
            art_count[art] = 1
    max_count = 0
    for el in art_count:
        if el + 1 in art_count:
            max_len = art_count[el] + art_count[el+1]
            max_count = max(max_count, max_len)

    return max_count


class Test(unittest.TestCase):
    def test1(self):
        art_pieces1 = [1, 3, 2, 2, 5, 2, 3, 7]
        return self.assertEqual(find_balanced_subsequence(art_pieces1), 5)

    def test2(self):
        art_pieces1 = [1, 2, 3, 4]
        return self.assertEqual(find_balanced_subsequence(art_pieces1), 2)

    def test3(self):
        art_pieces1 = [1, 1, 1, 1]
        return self.assertEqual(find_balanced_subsequence(art_pieces1), 0)


if __name__ == "__main__":
    unittest.main()
# Example Usage:

#  art_pieces1 ={
#      1:1,
#      3:2,

#  }
# art_pieces1 = [1, 3, 2, 2, 5, 2, 3, 7]
# art_pieces2 = [1, 2, 3, 4]
# art_pieces3 = [1, 1, 1, 1]

# print(find_balanced_subsequence(art_pieces1))
# print(find_balanced_subsequence(art_pieces2))
# print(find_balanced_subsequence(art_pieces3))
# Example Output:

# 5
# Example 1 Explanation:  The longest balanced subsequence is [3, 2, 2, 2, 3].

# 2
# 0
