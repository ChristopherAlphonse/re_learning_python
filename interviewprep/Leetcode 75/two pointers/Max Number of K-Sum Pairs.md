Relevant link: [Max Number of K-Sum Pairs](https://leetcode.com/problems/max-number-of-k-sum-pairs/)

You are given an integer array `nums` and an integer `k`.

In one operation, you can pick two numbers from the array whose sum equals `k` and remove them from the array.

Return _the maximum number of operations you can perform on the array_.

**Example 1:**

**Input:** nums = [1,2,3,4], k = 5
**Output:** 2
**Explanation:** Starting with nums = [1,2,3,4]:
- Remove numbers 1 and 4, then nums = [2,3]
- Remove numbers 2 and 3, then nums = []
There are no more pairs that sum up to 5, hence a total of 2 operations.

**Example 2:**

**Input:** nums = [3,1,3,4,3], k = 6
**Output:** 1
**Explanation:** Starting with nums = [3,1,3,4,3]:
- Remove the first two 3's, then nums = [1,4,3]
There are no more pairs that sum up to 6, hence a total of 1 operation.

**Constraints:**

- `1 <= nums.length <= 105`
- `1 <= nums[i] <= 109`
- `1 <= k <= 109`


[Solution]
```python
class Solution:

    def maxOperations(self, nums: list[int], k: int) -> int:

        occurrence = 0
        left = 0
        right = len(nums) - 1
        nums.sort()

        if len(nums) <= 1:
            return occurrence

  
        while left < right:
            total_sum = nums[left] + nums[right
            
            if total_sum == k:
                occurrence += 1
                left += 1
                right -= 1
            elif total_sum > k:
                right -= 1
            else:
                left += 1

        return occurrence
        
```
