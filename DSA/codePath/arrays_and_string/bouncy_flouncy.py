# Problem 2: Bouncy, Flouncy, Trouncy, Pouncy
# Tigger has developed a new programming language Tiger with only four operations and one variable tigger.

# bouncy and flouncy both increment the value of the variable tigger by 1.
# trouncy and pouncy both decrement the value of the variable tigger by 1.
# Initially, the value of tigger is 1 because he's the only tigger around! Given a list of strings operations containing a list of operations, return the final value of tigger after performing all the operations.

import unittest


def final_value_after_operations(operations):
    res = 1
    for op in operations:
        if op == "bouncy" or op == "flouncy":
            res += 1
        elif op == "trouncy" or op == "pouncy":
            res -= 1
    return res


class Test(unittest.TestCase):
    def test1(self):
        operations = ["trouncy", "flouncy", "flouncy"]
        return self.assertEqual(final_value_after_operations(operations), 2)

    def tes2(self):
        operations = ["bouncy", "bouncy", "flouncy"]
        return self.assertEqual(final_value_after_operations(operations), 4)


if __name__ == "__main__":
    unittest.main()
