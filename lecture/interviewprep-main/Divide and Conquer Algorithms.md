# Divide and Conquer Algorithms

The three sorting algorithms we've seen so far, bubble sort, selection sort, and insertion sort, have worst-case running times of O(n^2). When the size of the input array is large, these algorithms can take a long time to run.
![image](https://img-c.udemycdn.com/redactor/raw/2020-10-14_13-16-08-f55bea0446e093cbb075cb533b202d24.png)

From this lecture, we'll see two other sorting algorithms, quicksort and merge sort, whose running times are better. In particular, merge sort runs in O(n*logn) time in all cases, and quicksort runs in O(n*logn) time in the best case and on average, though its worst-case running time is O(n^2). Here's a table of these five sorting algorithms and their running times:

### Divide-and-conquer

Both merge sort and quicksort employ a common algorithmic paradigm based on recursion. This paradigm, divide-and-conquer, breaks a problem into sub-problems that are similar to the original problem, recursively solves the sub-problems, and finally combines the solutions to the sub-problems to solve the original problem. Because divide-and-conquer solves sub-problems recursively, each subproblem must be smaller than the original problem, and there must be a base case for sub-problems. You should think of a divide-and-conquer algorithm as having three parts:

Divide the problem into a number of sub-problems that are smaller instances of the same problem.

Conquer the sub-problems by solving them recursively. If they are small enough, solve the sub-problems as base cases.

Combine the solutions to the sub-problems into the solution for the original problem.

You can easily remember the steps of a divide-and-conquer algorithm as divide, conquer, combine. Here's how to view one step, assuming that each divide step creates two sub-problems (though some divide-and-conquer algorithms create more than two):
![](https://img-c.udemycdn.com/redactor/raw/2020-10-14_13-25-21-9b0f30214888924dcb6b98015ea78367.png)
If we expand out two more recursive steps, it looks like this:
![](https://img-c.udemycdn.com/redactor/raw/2020-10-14_13-49-15-285dc4b9f10986d926e8814713342ef9.png)
Because divide-and-conquer creates at least two sub-problems, a divide-and-conquer algorithm makes multiple recursive calls.
