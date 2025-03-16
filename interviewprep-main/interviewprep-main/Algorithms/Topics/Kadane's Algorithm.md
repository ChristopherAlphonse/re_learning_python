# Kadane's Algorithm

Find the largest sum of any contiguous subarray.

```python
def max_subarray(numbers):
    best_sum = float("-inf")
    current_sum = 0
    for x in numbers:
        current_sum = max(0, current_sum + x)
        best_sum = max(best_sum, current_sum)
    return best_sum
```

