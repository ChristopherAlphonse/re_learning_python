# Problem 1: Hunny Hunt
# Write a function linear_search() to help Winnie the Pooh locate his lost items. The function accepts a list items and a target value as parameters. The function should return the first index of target in items, and -1 if target is not in the lst. Do not use any built-in functions.
import unittest


def linear_search(lst, target):
    for index, item in enumerate(lst):
        if item == target:
            return index
    return -1


class Test(unittest.TestCase):

    def test1(self):
        items = ['haycorn', 'haycorn', 'haycorn', 'hunny', 'haycorn']
        target = 'hunny'
        return self.assertEqual(linear_search(items, target), 3)

    def test2(self):
        items = ['bed', 'blue jacket', 'red shirt', 'hunny']
        target = 'red balloon'
        return self.assertEqual(linear_search(items, target), -1)


if __name__ == '__main__':
    unittest.main()
