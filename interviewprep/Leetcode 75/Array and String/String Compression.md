Relevant link: [443. String Compression](https://leetcode.com/problems/string-compression/) , [Run Length Encoding]( https://en.wikipedia.org/wiki/Run-length_encoding)

Given an array of characters `chars`, compress it using the following algorithm:

Begin with an empty string `s`. For each group of **consecutive repeating characters** in `chars`:

- If the group's length is `1`, append the character to `s`.
- Otherwise, append the character followed by the group's length.

The compressed string `s` **should not be returned separately**, but instead, be stored **in the input character array `chars`**. Note that group lengths that are `10` or longer will be split into multiple characters in `chars`.
ss
After you are done **modifying the input array,** return _the new length of the array_.

You must write an algorithm that uses only constant extra space.

**Example 1:**

**Input:** chars = ["a","a","b","b","c","c","c"]
**Output:** Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]
**Explanation:** The groups are "aa", "bb", and "ccc". This compresses to "a2b2c3".

**Example 2:**

**Input:** chars = ["a"]
**Output:** Return 1, and the first character of the input array should be: ["a"]
**Explanation:** The only group is "a", which remains uncompressed since it's a single character.

**Example 3:**

**Input:** chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
**Output:** Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].
**Explanation:** The groups are "a" and "bbbbbbbbbbbb". This compresses to "ab12".

**Constraints:**

- `1 <= chars.length <= 2000`
- `chars[i]` is a lowercase English letter, uppercase English letter, digit, or symbol.

[Solution]


```python
# optimal
# time 0(n) space(1)  
class Solution:

    def compress(self, chars: List[str]) -> int:
        write = 0
        count = 1
        n = len(chars)


        for index in range(1, n + 1):

            if index == n or chars[index] != chars[index - 1]:
                chars[write] = chars[index - 1]
                write += 1


                if count > 1:
                    for number in str(count):
                        chars[write] = number
                        write += 1
                count = 1
                
            else:
                count += 1
        return write
```


```python

# preffered
# time 0(n) space 0(n)

def rle(string_to_compress):
    result = []
    count = 1
    
    for index in range(1, len(string_to_compress)):
        if string_to_compress[index] == string_to_compress[index - 1]:
            count += 1
        else:
            result.append(f"{string_to_compress[index - 1]} {count}")
            count = 1
    
    result.append(f"{string_to_compress[index - 1]} {count}")
    return (result)
		
		
```