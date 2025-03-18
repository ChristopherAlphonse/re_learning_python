class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        if n == 0:
            return True
        length = len(flowerbed)
        for i in range(length):
            left = (i == 0) or (flowerbed[i - 1] == 0)
            right = (i == length - 1) or flowerbed[i + 1] == 0

            if left and right and flowerbed[i] == 0:
                flowerbed[i] = 1
                n -= 1

                if n == 0:
                    return True

        return False


flowerbed = [1, 0, 0, 0, 1]
n = 2
solution = Solution()
print(solution.canPlaceFlowers(flowerbed, n))
