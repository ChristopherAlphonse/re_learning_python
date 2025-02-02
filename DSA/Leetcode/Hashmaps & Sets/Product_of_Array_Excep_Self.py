def productExceptSelf(nums):
    result = [0] * len(nums)

    prefix = 1
    for index, value in enumerate(nums):
        result[index] = prefix
        prefix *= value

    postfix = 1
    for index in range(len(nums) - 1, -1, -1):
        result[index] *= postfix
        postfix *= nums[index]

    return result


nums = [1, 2, 3, 4]
print(productExceptSelf(nums))
# expected Output: [24,12,8,6]
