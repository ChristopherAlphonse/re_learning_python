# Problem 4: Non-decreasing Array
# Given an array nums with n integers,
# write a function non_decreasing() that checks if nums could become non-decreasing by modifying at most one element.

# We define an array is non-decreasing if nums[i] <= nums[i + 1] holds for every i(0-based) such that(0 <= i <= n - 2).


# if modified more than 1 return False

def non_decreasing(nums):
    modified = False
    for i in range(len(nums)-1):
        if nums[i] <= nums[i + 1]:
            continue
        if modified:
            return False

        if i == 0 or nums[i+1] >= nums[i-1]:
            nums[i] = nums[i+1]
        else:
            nums[i+1] = nums[i]
            modified = True
    return True


nums = [3, 4, 2, 3]
print(non_decreasing(nums))
# HAPPY CASE
# Input: [4, 2, 3]
# Expected Output: True
# Explanation: Modify 4 to 1 to get the array[1, 2, 3], which is non-decreasing.

# Input: [3, 4, 2, 3]
# Expected Output: False
# Explanation: More than one modification is needed to make the array non-decreasing.

# EDGE CASE
# Input: [1, 2, 3]
# Expected Output: True
# Explanation: The array is already non-decreasing, so no modification is needed.
