
# Boyer Moore Majority Vote Algorithm


# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.


# Example 1:
# Input: nums = [3, 2, 3]
# Output: 3

# Example 2:
# Input: nums = [2, 2, 1, 1, 1, 2, 2]
# Output: 2

def majorityElement(nums):
    count = 0
    candidate = 0
    for n in nums:
        if count == 0:
            candidate = n
        count += 1 if n == candidate else -1
    return candidate


nums = [6, 5, 5]
print(majorityElement(nums))
