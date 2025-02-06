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
        start = 0
        end = len(s)-1
        while start < end:
            if not self.isAlphaNum(s[start]):
                start += 1
                continue
            elif not self.isAlphaNum(s[end]):
                end -= 1
                continue
            elif s[start].lower() != s[end].lower():
                return False
            else:
                start += 1
                end -= 1
        return True

    def isAlphaNum(self, s: str) -> bool:
        return (
            (ord('a') <= ord(s) <= ord('z')) or
            (ord('A') <= ord(s) <= ord('Z')) or
            (ord('0') <= ord(s) <= ord('9'))
        )


s2 = "A man, a plan, a canal: Panama"
s = "race a car"
s3 = " "
sol = Solution()
print(sol.isPalindrome(s2))
print(sol.isPalindrome(s))
print(sol.isPalindrome(s3))
