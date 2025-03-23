[Topic] #two-pointer #string 

Relevant link: [345. Reverse Vowels of a String](https://leetcode.com/problems/reverse-vowels-of-a-string/)

Given a string `s`, reverse only all the vowels in the string and return it.

The vowels are `'a'`, `'e'`, `'i'`, `'o'`, and `'u'`, and they can appear in both lower and upper cases, more than once.

**Example 1:**

**Input:** s = "IceCreAm"

**Output:** "AceCreIm"

**Explanation:**

The vowels in `s` are `['I', 'e', 'e', 'A']`. On reversing the vowels, s becomes `"AceCreIm"`.

**Example 2:**

**Input:** s = "leetcode"

**Output:** "leotcede"

**Constraints:**

- `1 <= s.length <= 3 * 105`
- `s` consist of **printable ASCII** characters.

[Solution]

```python
class Solution:
    def reverseVowels(self, s: str) -> str:
        string = list(s)
        left, right = 0, len(s) - 1

        while left < right:
            while left < right and not isVowel(string[left]):
                left += 1
            while left < right and not isVowel(string[right]):
                right -= 1

            
            string[left], string[right] = string[right], string[left]
            left += 1
            right -= 1

        return ''.join(string)


def isVowel(char: str) -> bool:
    vowels = "aeiouAEIOU"
    return len(char) == 1 and ord('A') <= ord(char) <= ord('z') and char in vowels

```


### Lesson Learned

initially when updating my pointers i was doing so twice, I thought it would be fine to update the pointers in the while loop block,  took 2-5minuts to realized I should immediately update my pointers after a swap 