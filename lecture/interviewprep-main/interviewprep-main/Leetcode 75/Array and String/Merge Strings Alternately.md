[Topic] #two-pointer #string

You are given two strings `word1` and `word2`. Merge the strings by adding letters in alternating order, starting with `word1`. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return _the merged string._

**Example 1:**

**Explanation:** The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r

**Example 2:**

**Explanation:** Notice that as word2 is longer, "rs" is appended to the end.
word1:  a   b 
word2:    p   q   r   s
merged: a p b q   r   s

**Example 3:**


**Explanation:** Notice that as word1 is longer, "cd" is appended to the end.
word1:  a   b   c   d
word2:    p   q 
merged: a p b q c   d

**Constraints:**

- `1 <= word1.length, word2.length <= 100`
- `word1` and `word2` consist of lowercase English letters

[Solution]

``` python

class Solution: 
	def mergeAlternately(self, word1: str, word2: str) -> str: 
	res = [] 
	for i in range(max(len(word1), len(word2))):
		if i < len(word1) and i < len(word2): 
			res.append(word1[i] + word2[i]) 
		else:
			if i < len(word2): 
				res.extend(word2[i:]) 
				break 
			else: 
				res.extend(word1[i:]) 
				break
	return "".join(res)
```
[Reasoning]

#### My Intuition

	I need a way to store my values and weighted the benefits of a list vs contantly updating a inmutable string

#### My Plan

2. Created a `for loop` and the length of the loops will whichever is the longest string
3. I added all characters up to when the length of a string stop being the same
4. I determined which input is the longest and which ever if, I append the remainder


