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

        word = list(s)

        left = 0

        right = len(s) - 1

        v_bank = "aeiouAEIOU"

  

        while left < right:

            if word[left] in v_bank and word[right] in v_bank:

                word[left], word[right] = word[right], word[left]

                left += 1

                right -= 1

            elif word[left] not in v_bank:

                left += 1

            else:

                right -= 1

  

        return "".join(word)
```


### Lesson Learned

initially when updating my pointers i was doing so twice, I thought it would be fine to update the pointers in the while loop block,  took 2-5minuts to realized I should immediately update my pointers after a swap 