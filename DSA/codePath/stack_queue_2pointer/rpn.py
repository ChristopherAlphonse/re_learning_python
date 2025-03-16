# 150. Evaluate Reverse Polish Notation
# You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

# Evaluate the expression. Return an integer that represents the value of the expression.

# Note that:

# The valid operators are '+', '-', '*', and '/'.
# Each operand may be an integer or another expression.
# The division between two integers always truncates toward zero.
# There will not be any division by zero.
# The input represents a valid arithmetic expression in a reverse polish notation.
# The answer and all the intermediate calculations can be represented in a 32-bit integer.


# Example 1:

# Input: tokens = ["2", "1", "+", "3", "*"]
# Output: 9
# Explanation: ((2 + 1) * 3) = 9

import unittest


class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        operators = {'+', '-', '*',  '/'}

        for t in tokens:
            if t in operators:
                b, a = stack.pop(), stack.pop()
                match t:
                    case '+':
                        stack.append(a + b)
                    case '-':
                        stack.append(a - b)
                    case '*':
                        stack.append(a * b)
                    case '/':
                        stack.append(int(a / b))
            else:
                stack.append(int(t))
        return stack.pop()


case3 = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
case2 = ["4", "13", "5", "/", "+"]
case1 = ["2", "1", "+", "3", "*"]


class Test(unittest.TestCase):
    def test1(self):
        return self.assertEqual(Solution().evalRPN(case1), 9)

    def test2(self):
        return self.assertEqual(Solution().evalRPN(case2), 6)

    def test3(self):
        return self.assertEqual(Solution().evalRPN(case3), 22)


if __name__ == "__main__":

    unittest.main()
