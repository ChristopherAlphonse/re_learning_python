import unittest
# Problem 3: T-I-Double Guh-Er II
# T-I-Double Guh-Er: That spells Tigger! Write a function tiggerfy() that accepts a string word and returns a new string that removes any substrings t, i, gg, and er from word. The function should be case insensitive.


def tiggerfy(word):
    word_lower = word.lower()
    word_bank = ["t", "i", "gg", "er"]

    for sub in word_bank:
        if sub in word_lower:
            word_lower = word_lower.replace(sub, "")

    return word_lower


class Test(unittest.TestCase):
    def test1(self):
        word = "Trigger"
        return self.assertEqual(tiggerfy(word), "r")

    def test2(self):
        word = "eggplant"
        return self.assertEqual(tiggerfy(word), "eplan")


if __name__ == "__main__":
    unittest.main()
