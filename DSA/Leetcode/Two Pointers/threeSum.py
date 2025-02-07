# 3Sum

# Given an integer array nums, return all the triplets[nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.


# Example 1:
# Input: nums = [-1, 0, 1, 2, -1, -4]
# Output: [[-1, -1, 2], [-1, 0, 1]]
# Explanation:
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are[-1, 0, 1] and [-1, -1, 2].
# Notice that the order of the output and the order of the triplets does not matter.

# Example 2:
# Input: nums = [0, 1, 1]
# Output: []
# Explanation: The only possible triplet does not sum up to 0.

# Example 3:
# Input: nums = [0, 0, 0]
# Output: [[0, 0, 0]]
# Explanation: The only possible triplet sums up to 0.


# Constraints:

# 3 <= nums.length <= 3000
# -105 <= nums[i] <= 105

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        result = []
        nums.sort()
        target = 0

        for idx in range(n):
            if nums[idx] > target:
                break
            if idx > target and nums[idx] == nums[idx - 1]:
                continue

            left = idx + 1
            right = n - 1

            while left < right:
                curr_sum = nums[idx] + nums[left] + nums[right]
                if curr_sum == target:
                    result.append([nums[idx], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif curr_sum < target:
                    left += 1
                else:
                    right -= 1
        return result


nums = [-1, 0, 1, 2, -1, -4]
sol = Solution()
print(sol.threeSum(nums))


# Time 0(n^2) space 0(n)
