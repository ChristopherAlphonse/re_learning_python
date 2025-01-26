def findClosestNumber(nums):
    closest = nums[0]
    for el in nums:
        if abs(el) < abs(closest):
            closest = el
    if abs(closest) in nums and closest < 0:
        return abs(closest)
    return closest
