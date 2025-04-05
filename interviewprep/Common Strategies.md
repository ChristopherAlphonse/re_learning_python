
https://hackernoon.com/14-patterns-to-ace-any-coding-interview-question-c5bb3357f6ed

## [Cheat Sheet]

> 1.  IF sorted THEN (binary search OR two pointer)
> 2.  IF all permutations/subsets THEN backtracking
> 3.  IF tree THEN (recursion OR two pointer OR obvious recursion below)
> 4.  IF graph THEN dfs/bfs
> 5.  IF linkedlist $O(1)$ space THEN two pointer
> 6.  IF obvious recursion problem but recursion banned THEN stack
> 7.  IF options (+1 or +2) OR min/max + previously made choices THEN DP
> 8.  IF k items THEN heap
> 9.  IF common strings THEN (map OR trie)
> 10. ELSE (map/set for $O(n)$ time $O(n)$ space or sort for $O(n \cdot log \cdot n)$ time $O(1)$ space)

## [Multiple pointers]
*For problems involving arrays, strings, or linked lists, using two pointers (fast and slow) can often be helpful.*

``` mermaid
flowchart TD
    A["Start"] --> B["Initialize left pointer (L) at start"]
    B --> C["Initialize right pointer (R) at end"]
    C --> D{"Is L < R?"}
    D -- "Yes" --> E["Process elements at L and R"]
    E --> F["Move L to right (L = L + 1)"]
    F --> G["Move R to left (R = R - 1)"]
    G --> D
    D -- "No" --> H["Finish processing"]
```


Example:
```python
def move_pointers(arr):
    slow = 0
    fast = 0
    while fast < len(arr):
        if arr[fast] != arr[slow]:
            slow += 1
            arr[slow] = arr[fast]
        fast += 1
    return arr[:slow+1]
```

## [Iterating in Reverse]
*Some solutions require iterating from the end of the array. This is especially useful for string-related problems.*

Example:
```python
def reverse_iterate(arr):
    for i in range(len(arr)-1, -1, -1):
        print(arr[i])
```

## [Sorting and Binary Search]
*Sorting the input can often make a problem simpler, enabling the use of binary search.*

Example:
```python
def binary_search(arr, target):
    arr.sort()
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
```

## [Backtracking]
*Used when problems involve a series of choices, where each choice constrains subsequent choices. We try every possibility and "backtrack" when we reach a dead end.*

``` mermaid
graph TD

    A[Start] --> B[Find solution?]

    B -- Yes --> C[Output result]

    C --> D[Return]

    B -- No --> E[Iterate over candidates]

    E --> F[Is candidate valid?]

    F -- Yes --> G[Place candidate]

    G --> H[Call backtrack with candidate]

    H --> I[Backtrack remove candidate]

    F -- No --> E

    E --> D
```



**General Algorithm:**
```python
def backtrack(candidate):
    if find_solution(candidate):
        output(candidate)
        return
    
    for next_candidate in candidates:
        if is_valid(next_candidate):
            place(next_candidate)
            backtrack(next_candidate)
            remove(next_candidate)
```
**Example:** Find all combinations of `k` numbers that sum up to `n`:

```python
def combination_sum3(k, target):
    results = []
    backtrack(target, k, 1, results, [])
    return results

def backtrack(remain, k, start, results, comb):
    if remain == 0 and len(comb) == k:
        results.append(list(comb))
        return
    for i in range(start, 10):
        comb.append(i)
        backtrack(remain - i, k, i + 1, results, comb)
        comb.pop()
```

## [Greedy Algorithms]
*Greedy algorithms make locally optimal choices at each step, hoping they lead to a globally optimal solution. They are faster but may not always give the best result. 

``` mermaid
graph TD
    A[Start] --> B[Sort items by value-to-weight ratio]
    B --> C[Initialize total_value = 0]
    C --> D[For each item in sorted list]
    D --> E[Can the item fit?]
    E -- Yes --> F[Add item to total_value]
    F --> G[Reduce capacity]
    G --> D
    E -- No --> H[End loop]
    H --> I[Return total_value]

```
Example:
```python
def greedy_knapsack(weights, values, capacity):
    n = len(weights)
    ratio = [(v / w, v, w) for v, w in zip(values, weights)]
    ratio.sort(reverse=True)
    
    total_value = 0
    for r, v, w in ratio:
        if capacity >= w:
            capacity -= w
            total_value += v
        else:
            break
    return total_value
```

## [Divide and Conquer]
*Break the problem into smaller sub-problems, solve each sub-problem, and combine the results.

``` mermaid
graph TD
    A[Start] --> B[Is list length <= 1?]
    B -- Yes --> C[Return list]
    B -- No --> D[Split list into two halves]
    D --> E[Merge sort left half]
    D --> F[Merge sort right half]
    E --> G[Merge left and right]
    F --> G
    G --> H[Return merged list]

```

Example: **Merge Sort**
```python
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result
```

## [Dynamic Programming] (DP)
*Identify overlapping sub-problems and store the results to avoid redundant calculations.

### Fibonacci with Memorization:


```python
memo = {}

def fib(n):
    if n <= 2:
        return 1
    if n not in memo:
        memo[n] = fib(n - 1) + fib(n - 2)
    return memo[n]
```


### Knapsack Problem:

``` mermaid
graph TD

    A[Start] --> B[Create DP table with size n+1 x capacity+1]

    B --> C[For each item i from 1 to n]

    C --> D[For each capacity w from 0 to max capacity]

    D --> E{Is item i's weight <= current capacity?}

    E -->|Yes| F[Take maximum of previous or current item plus value]

    E -->|No| G[Carry forward previous result]

    F --> D

    G --> D

    D --> H[Return value of DP table at n and capacity]
```

```python
def knapsack(values, weights, capacity):
    dp = [[0] * (capacity + 1) for _ in range(len(values) + 1)]
    
    for i in range(1, len(values) + 1):
        for w in range(capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]
    return dp[len(values)][capacity]
```

## [Sliding Window]
*Sliding windows are used to reduce redundant calculations, especially for problems involving contiguous subarrays or substrings.

``` mermaid
graph TD

    A[Start] --> B[Initialize windowSize]

    B --> C[Set window start position = 0]

    C --> D(Check if window is within collection bounds)

    D -->|Yes| E[Process current window elements]

    E --> F[Increment window start position]

    F --> D

    D -->|No| G[End]
```
**Example:** Calculate the number of ways to climb a staircase with `maxSteps` at a time.
```python
def staircase_traversal(height, max_steps):
    ways = [0] * (height + 1)
    ways[0] = 1

    for i in range(1, height + 1):
        for j in range(1, max_steps + 1):
            if i - j >= 0:
                ways[i] += ways[i - j]
    return ways[height]
```
