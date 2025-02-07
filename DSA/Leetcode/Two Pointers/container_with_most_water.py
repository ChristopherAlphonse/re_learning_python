# Container With Most Water

# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are(i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store.

# Notice that you may not slant the container.


# Example 1:
# Input: height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
# Output: 49
# Explanation: The above vertical lines are represented by array[1, 8, 6, 2, 5, 4, 8, 3, 7]. In this case, the max area of water(blue section) the container can contain is 49.

# Example 2:
# Input: height = [1, 1]
# Output: 1


# Constraints:

# n == height.length
# 2 <= n <= 105
# 0 <= height[i] <= 104


class Solution:
    def maxArea(self, height: list[int]) -> int:
        left = 0
        right = len(height) - 1
        curr_max = 0
        while left < right:
            height_len = min(height[left], height[right])
            width = right - left
            area = width * height_len

            curr_max = max(curr_max, area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return curr_max


height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
sol = Solution()
print(sol.maxArea(height))

# width = number of elements from the two tallest points
# A = w *  h = 7*7 = 49


# Explanation:

# We can solve this question in linear time because we can eliminate containers as we search. After initializing our pointers at opposite ends of the array, the current container being considered is outlined in blue, which can hold a total of 16 units of water.
# We get 16 by taking the width of the container right - left and multiplying it by the height of the shorter wall Math.min(nums[left], nums[right]).

# Now, the question is: how can we advance to the next container in a way that eliminates unecessary containers from our search? Let's look at the volumes of all other containers ending at the right pointer )

# And the volumes of all other containers starting at the left pointer

# All other containers ending at the right pointer hold a smaller amount of water than our current container, so we eliminate them from our search by moving the right pointer.

# This gives us a new container with a volume of 49, which becomes the new maximum.
