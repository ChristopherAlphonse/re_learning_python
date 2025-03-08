# 682. Baseball Game

# You are keeping the scores for a baseball game with strange rules. At the beginning of the game, you start with an empty record.

# You are given a list of strings operations, where operations[i] is the ith operation you must apply to the record and is one of the following:

# An integer x.
# Record a new score of x.
# '+'.
# Record a new score that is the sum of the previous two scores.
# 'D'.
# Record a new score that is the double of the previous score.
# 'C'.
# Invalidate the previous score, removing it from the record.
# Return the sum of all the scores on the record after applying all the operations.

# The test cases are generated such that the answer and all intermediate calculations fit in a 32-bit integer and that all operations are valid.


# Example 1:

# Input: ops = ["5", "2", "C", "D", "+"]
# Output: 30
# Explanation:
# "5" - Add 5 to the record, record is now[5].
# "2" - Add 2 to the record, record is now[5, 2].
# "C" - Invalidate and remove the previous score, record is now[5].
# "D" - Add 2 * 5 = 10 to the record, record is now[5, 10].
# "+" - Add 5 + 10 = 15 to the record, record is now[5, 10, 15].
# The total sum is 5 + 10 + 15 = 30.


import unittest
from typing import List


class Solution:
    def numeric(self, s):
        return s.lstrip("-").isdigit()

    def calPoints(self, operations: List[str]) -> int:
        record = []

        for op in operations:
            if self.numeric(op):
                record.append(int(op))
            else:
                match op:
                    case "+":
                        if len(record) >= 2:
                            record.append(record[-1] + record[-2])
                    case "D":
                        if record:
                            record.append(record[-1] * 2)
                    case "C":
                        if record:
                            record.pop()
        return sum(record)


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_numeric(self):
        self.assertTrue(self.solution.numeric("123"))
        self.assertTrue(self.solution.numeric("-456"))
        self.assertFalse(self.solution.numeric("+789"))
        self.assertFalse(self.solution.numeric("abc"))
        self.assertFalse(self.solution.numeric("12a"))

    def test_calPoints_basic(self):
        self.assertEqual(self.solution.calPoints(
            ["5", "2", "C", "D", "+"]), 30)

    def test_calPoints_with_negatives(self):
        self.assertEqual(self.solution.calPoints(
            ["5", "-2", "4", "C", "D", "9", "+", "+"]), 27)

    def test_calPoints_only_numbers(self):
        self.assertEqual(self.solution.calPoints(
            ["1", "2", "3", "4", "5"]), 15)

    def test_calPoints_empty(self):
        self.assertEqual(self.solution.calPoints([]), 0)

    def test_calPoints_edge_cases(self):
        self.assertEqual(self.solution.calPoints(
            ["10", "C", "C"]), 0)


if __name__ == "__main__":
    unittest.main()
