#  Valid Palindrome

# A phrase is a palindrome if , after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.


# Example 1:

# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
# Example 2:

# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.
# Example 3:

# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric characters.
# Since an empty string reads the same forward and backward, it is a palindrome.


# Constraints:

# 1 <= s.length <= 2 * 105
# s consists only of printable ASCII characters.

class Solution:
    def isPalindrome(self, s: str) -> bool:
        start_index = 0
        end_index = len(s) - 1

        while start_index < end_index:
            while start_index < end_index and not self.isAlphaNumeric(s[start_index]):
                start_index += 1
            while end_index > start_index and not self.isAlphaNumeric(s[end_index]):
                end_index -= 1
            if s[start_index].lower() != s[end_index].lower():
                return False
            start_index += 1
            end_index -= 1
        return True

    def isAlphaNumeric(self, char: str) -> bool:
        return (ord('A') <= ord(char) <= ord('Z') or
                ord('a') <= ord(char) <= ord('z') or
                ord('0') <= ord(char) <= ord('9'))


s2 = "A man, a plan, a canal: Panama"
s = "race a car"
s3 = " "
sol = Solution()
print(sol.isPalindrome(s2))
print(sol.isPalindrome(s))
print(sol.isPalindrome(s3))
