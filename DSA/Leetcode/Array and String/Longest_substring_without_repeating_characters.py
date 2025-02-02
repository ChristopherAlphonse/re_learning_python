# Longest Substring Without Repeating Characters

# Given a string s, find the length of the longest
# substring
# without repeating characters.

# Example 1:
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

# Example 2:
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.

# Example 3:
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        store = set()
        longest_sub_str = 0
        left = 0

        for right, char in enumerate(s):
            while char in store:
                store.remove(s[left])
                left += 1
            store.add(char)
            sliding_window = (right - left) + 1
            longest_sub_str = max(longest_sub_str, sliding_window)
        return longest_sub_str


s = "pwwkew"
solution = Solution()
print(solution.lengthOfLongestSubstring(s))
