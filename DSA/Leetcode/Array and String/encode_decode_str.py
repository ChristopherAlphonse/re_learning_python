# Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.

# Please implement encode and decode

# Input: ["lint", "code", "love", "you"]
# Output: ["lint", "code", "love", "you"]
# Explanation:
# One possible encode method is : "lint:;code:;love:;you"


# Input: ["we", "say", ":", "yes"]
# Output: ["we", "say", ":", "yes"]
# Explanation:
# One possible encode method is : "we:;say:;:::;yes"

class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """

    def encode(self, strs):
        res = ""
        for st in strs:
            res = f"{len(st)}#{st}"
        return res
    """
    @param: str: A string
    @return: decodes a single string to a list of strings
    """

    def decode(self, s: str):
        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length  # point to the end of the current string
            res.append(s[i:j])  # extract substring from i-j
            i = j

        return res


ans = Solution()
print(ans.encode(["we", "say", ":", "yes"]))
print(ans.decode(ans.encode(["we", "say", ":", "yes"])))
