def topKFrequent(nums, k):
    num_count = {}
    frequency_buckets = [[] for i in range(len(nums) + 1)]

    for el in nums:
        num_count[el] = num_count.get(el, 0) + 1

    for num, count in num_count.items():
        frequency_buckets[count].append(num)

    response = []
    # iterate backwards to process the most frequent elements first
    for index in range(len(frequency_buckets) - 1, 0, -1):
        for num in frequency_buckets[index]:
            print(num)
            response.append(num)
            if len(response) == k:
                return response


nums = [1, 2, 2, 3, 3, 3]
k = 2
# Expected Output: [2, 3]
print(topKFrequent(nums, k))
