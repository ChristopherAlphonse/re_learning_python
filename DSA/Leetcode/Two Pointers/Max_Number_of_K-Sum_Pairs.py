class Solution:
    def maxOperations(self, nums: list[int], k: int) -> int:
        occurrence = 0
        left = 0
        right = len(nums) - 1
        nums.sort()
        if len(nums) <= 1:
            return occurrence

        while left < right:
            total_sum = nums[left] + nums[right]
            if total_sum == k:
                occurrence += 1
                left += 1
                right -= 1
            elif total_sum > k:
                right -= 1
            else:
                left += 1
        return occurrence


nums = [4, 4, 1, 3, 1, 3, 2, 2, 5, 5, 1, 5, 2, 1, 2, 3, 5, 4]
k = 2
sol = Solution()
print(sol.maxOperations(nums, k))
