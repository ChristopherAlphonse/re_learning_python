class Solution:
    def compress(self, chars: list[str]) -> int:
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


chars = ["a", "a", "b", "b", "c", "c", "c"]
new_length = Solution().compress(chars)
print("Compressed:", chars[:new_length])
print("New length:", new_length)
