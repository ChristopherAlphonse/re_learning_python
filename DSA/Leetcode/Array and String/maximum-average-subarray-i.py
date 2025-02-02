# Maximum Average Subarray I

# You are given an integer array nums consisting of n elements, and an integer k.
# Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.


# Example 1:

# Input: nums = [1, 12, -5, -6, 50, 3], k = 4
# Output: 12.75000
# Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
# Example 2:

# Input: nums = [5], k = 1
# Output: 5.00000


class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        current_sum = sum(nums[:k])
        max_avrg = current_sum
        for index in range(k, len(nums)):
            # current_sum -> [50, 3] - [1 , 12] -> [49, -9]
            current_sum += nums[index] - nums[index-k]
            max_avrg = max(max_avrg, current_sum)
            return max_avrg / k


nums = [1, 12, -5, -6, 50, 3]
k = 4
solution = Solution()
print(solution.findMaxAverage(nums, k))
