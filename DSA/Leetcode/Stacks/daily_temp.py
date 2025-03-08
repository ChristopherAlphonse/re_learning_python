# 739. Daily Temperatures
# Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.


# Example 1:

# Input: temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
# Output: [1, 1, 4, 2, 1, 1, 0, 0]


class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        """
            Understand:
            we have a list of temperatures in non increasing order
            [current_index] loop through until i find a value bigger , calculate the distance otherwise return zero that was the last warm day
                I: list[int]
                O: list[int]
        """
        res = [0] * len(temperatures)
        stack = []

        for index, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                prev_index = stack.pop()
                res[prev_index] = index - prev_index
            stack.append(index)
        return res
