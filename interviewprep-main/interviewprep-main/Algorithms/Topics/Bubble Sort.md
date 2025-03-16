# Bubble Sort

### Explanation

```javascript
[8, 5, 2, 9, 5, 6, 3];
```

Given an unsorted array, we iterate through the array and compare each item to the next item. If we find that the first item is larger than the second item, we swap them.

This causes the largest number in the set to "bubble up" to the end of the array. This also means on each pass, we _know_ that the last number is the largest, so we can decrement a pointer from the end of the array and slowly shrink the comparison set.

We repeat this over and over until the array is sorted.

### Big O

Best case with a sorted array - $O(n)$
Worst case - $O(n^2)$

### Implementation

```kotlin
fun bubbleSort(array: MutableList<Int>): List<Int> {
    var endPointer = array.size - 1

 while (endPointer > 0) {
  for (index in 0 until endPointer) {
   val firstItem = array[index]
   val secondItem = array[index + 1]
   if (firstItem > secondItem) {
    array[index] = secondItem
    array[index + 1] = firstItem
   }
  }

  endPointer--
 }

    return array
}
```

# Bubble Sort Step-by-Step

We start with the unsorted array:

\[
\begin{array}{ccccccc}
8 & 5 & 2 & 9 & 5 & 6 & 3
\end{array}
\]

After each pass, the largest unsorted element bubbles up to its correct position.

\[
\begin{array}{ccccccc}
8  & 5  & 2  & 9  & 5  & 6  & 3  \\
5  & 8  & 2  & 9  & 5  & 6  & 3  \\
5  & 2  & 8  & 9  & 5  & 6  & 3  \\
5  & 2  & 8  & 5  & 9  & 6  & 3  \\
5  & 2  & 8  & 5  & 6  & 9  & 3  \\
5  & 2  & 8  & 5  & 6  & 3  & 9  \\
\hline
5  & 2  & 8  & 5  & 6  & 3  & 9  \\
2  & 5  & 8  & 5  & 6  & 3  & 9  \\
2  & 5  & 5  & 8  & 6  & 3  & 9  \\
2  & 5  & 5  & 6  & 8  & 3  & 9  \\
2  & 5  & 5  & 6  & 3  & 8  & 9  \\
\hline
2  & 5  & 5  & 6  & 3  & 8  & 9  \\
2  & 5  & 5  & 6  & 3  & 8  & 9  \\
2  & 5  & 5  & 3  & 6  & 8  & 9  \\
\hline
2  & 5  & 5  & 3  & 6  & 8  & 9  \\
2  & 5  & 3  & 5  & 6  & 8  & 9  \\
\hline
2  & 3  & 5  & 5  & 6  & 8  & 9  \\
\end{array}
\]

