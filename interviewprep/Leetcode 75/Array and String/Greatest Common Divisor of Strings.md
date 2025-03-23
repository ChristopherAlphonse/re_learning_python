[Topic] #Math #string

Relevant link: <https://en.wikipedia.org/wiki/Euclidean_algorithm> , <https://docs.python.org/3/library/math.html>

For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

Example 1:

Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"
Example 2:

Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"
Example 3:

Input: str1 = "LEET", str2 = "CODE"
Output: ""

**Constraints:**

-   `1 <= str1.length, str2.length <= 1000`
-   `str1` and `str2` consist of English uppercase letters.

[Solution]

```python

class Solution:

    def gcdOfStrings(self, str1: str, str2: str) -> str:

        if str1 + str2 != str2 + str1:
            return ""


        def calculate_gcd(a, b):
            while b:
                a , b = b , a % b
            return a       
           
        remainder = calculate_gcd(len(str1), len(str2))
        return str1[:remainder]
```

### Euclidean Algorithm

The algorithm works by repeatedly replacing the larger number with the remainder of dividing the larger number by the smaller number, and continuing until one of the numbers becomes zero. The non-zero number at that point is the GCD.

Example: Finding the GCD of 48 and 18
Let's go through the algorithm with a = 48 and b = 18.

Initial Values:

a = 48
b = 18
First Iteration (a = 48, b = 18):

We compute a % b, which is 48 % 18 = 12.
Now, the values of a and b are updated:
a = b = 18
b = a % b = 12
So, after the first iteration, we have:

a = 18
b = 12
Second Iteration (a = 18, b = 12):

We compute a % b, which is 18 % 12 = 6.
Now, the values of a and b are updated again:
a = b = 12
b = a % b = 6
So, after the second iteration, we have:

a = 12
b = 6
Third Iteration (a = 12, b = 6):

We compute a % b, which is 12 % 6 = 0.
Now, the values of a and b are updated:
a = b = 6
b = a % b = 0
So, after the third iteration, we have:

a = 6
b = 0
Termination:

Since b = 0, the loop terminates, and the function returns the current value of a, which is 6.
