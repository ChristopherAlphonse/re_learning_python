
def twoSum(nums, target):
    result = {}
    for index in range(len(nums)):
        # update value to the latest
        result[nums[index]] = index

    for element in range(len(nums)):
        compliment = target - nums[element]
        # if compliment in result we have our sum but it must not be the index we are currently at
        if compliment in result and result[compliment] != element:
            return [result[compliment], element]


nums = [2, 7, 11, 15]
target = 9
print(twoSum(nums, target))


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = {}
        for index in range(len(nums)):
            # update value to the latest
            result[nums[index]] = index

        for element in range(len(nums)):
            compliment = target - nums[element]
            # if compliment in result we have our sum but it must not be the index we are currently at
            if compliment in result and result[compliment] != element:
                return [result[compliment], element]
