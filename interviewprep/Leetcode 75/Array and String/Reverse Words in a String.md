
Relevant link:  [151. Reverse Words in a String](https://leetcode.com/problems/reverse-words-in-a-string/)

Given an input string `s`, reverse the order of the **words**.

A **word** is defined as a sequence of non-space characters. The **words** in `s` will be separated by at least one space.

Return _a string of the words in reverse order concatenated by a single space._

**Note** that `s` may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

**Example 1:**

**Input:** s = "the sky is blue"
**Output:** "blue is sky the"

**Example 2:**

**Input:** s = "  hello world  "
**Output:** "world hello"
**Explanation:** Your reversed string should not contain leading or trailing spaces.

**Example 3:**

**Input:** s = "a good   example"
**Output:** "example good a"
**Explanation:** You need to reduce multiple spaces between two words to a single space in the reversed string.

**Constraints:**

- `1 <= s.length <= 104`
- `s` contains English letters (upper-case and lower-case), digits, and spaces `' '`.
- There is **at least one** word in `s`.

**Follow-up:** If the string data type is mutable in your language, can you solve it **in-place** with `O(1)` extra space?

[Solution]

```python
# optimal
class Solution:
    def reverseWords(self, s: str) -> str:
        
        s = list(s)  
        self.reverse(s, 0, len(s) - 1)
        start = 0
        
        for end in range(len(s) + 1):
            if end == len(s) or s[end] == ' ': 
                self.reverse(s, start, end - 1)
                start = end + 1    
        return "".join(s) 
    
    def reverse(self, s, left, right):
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

```

```python
# preffered for readibilty 
class Solution:

    def reverseWords(self, s: str) -> str:
        words = s.split()
        return self.reverseStrings(words)

  

    def reverseStrings(self, s):
        left = 0
        right = len(s) - 1

        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

        return " ".join(s)
```
