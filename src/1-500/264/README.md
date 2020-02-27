# 264. Ugly number II
Write a program to find the n-th ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. 

## Example:

``` Python
Input: n = 10
Output: 12
Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.
```
## Note:  

* 1 is typically treated as an ugly number.
* n does not exceed 1690.

# Analysis

Here is a time efficient solution with O(n) extra space. The ugly-number sequence is 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, …
because every number can only be divided by 2, 3, 5, one way to look at the sequence is to split the sequence to three groups as below:

     (1) 1×2, 2×2, 3×2, 4×2, 5×2, …
     (2) 1×3, 2×3, 3×3, 4×3, 5×3, …
     (3) 1×5, 2×5, 3×5, 4×5, 5×5, …

We can find that every subsequence is the ugly-sequence itself (1, 2, 3, 4, 5, …) multiply 2, 3, 5. Then we use similar merge method as merge sort, to get every ugly number from the three subsequence. Every step we choose the smallest one, and move one step after.

## Source code
```python
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly = [0] * n
        ugly[0] = 1
        i2, i3, i5 = 1, 1, 1
        num2, num3, num5 = 2, 3, 5
        for i in range(1, n):
            ugly[i] = min(num2, num3, num5)
            if ugly[i] == num2:
                num2 = ugly[i2] * 2
                i2 += 1
            if ugly[i] == num3:
                num3 = ugly[i3] * 3
                i3 += 1
            if ugly[i] == num5:
                num5 = ugly[i5] * 5
                i5 += 1
        return ugly[-1]
```

## Complexity
* Time complexity: O(n)
* Space complexity: O(n)