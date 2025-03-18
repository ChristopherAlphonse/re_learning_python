[Topic] #array #greedy

Relevant link: [605. Can Place Flowers](https://leetcode.com/problems/can-place-flowers/)

You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in **adjacent** plots.

Given an integer array `flowerbed` containing `0`'s and `1`'s, where `0` means empty and `1` means not empty, and an integer `n`, return `true` *if* `n` *new flowers can be planted in the* `flowerbed` *without violating the no-adjacent-flowers rule and* `false` *otherwise*.

**Example 1:**

**Input:** flowerbed = [1,0,0,0,1], n = 1
**Output:** true

**Example 2:**

**Input:** flowerbed = [1,0,0,0,1], n = 2
**Output:** false

**Constraints:**

-   `1 <= flowerbed.length <= 2 * 104`
-   `flowerbed[i]` is `0` or `1`.
-   There are no two adjacent flowers in `flowerbed`.
-   `0 <= n <= flowerbed.length`

[Solution]

```python
class Solution:

    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        if n == 0:
            return True

        length = len(flowerbed)

        for i in range(length):
            left = (i == 0) or (flowerbed[i - 1] == 0)
            right = (i == length - 1) or  flowerbed[i + 1] == 0


            if left and right and flowerbed[i] == 0:
                flowerbed[i] = 1
                n -= 1

                if n == 0:
                    return True

        return False
```

1. Initial thought was n was to account for space needed i.e "can place flowers `n` space in between" thinking my solution was to account for different plants needing difference `n` size of space.

2. I thought i could use a fixed size sliding window of size 3 and if the sum is 0 then that means i can go ahead and plant a flower in the middle, but that dream came to an end when met against this [0,0,1,0,1] list. My window was no longer valid and my logic was flawed.

3. to account for out of bound i ensure left stop at 0 and right stop at the last index while checking the adjacent element.
