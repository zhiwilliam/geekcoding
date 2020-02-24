# 263. Ugly number
Write a program to check whether a given number is an ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.

## Example 1:

```Python
Input: 6
Output: true
Explanation: 6 = 2 × 3
```

## Example 2:

```Python
Input: 8
Output: true
Explanation: 8 = 2 × 2 × 2
```

## Example 3:

```python
Input: 14
Output: false 
Explanation: 14 is not ugly since it includes another prime factor 7.
```

## Note:

1. 1 is typically treated as an ugly number.
2. Input is within the 32-bit signed integer range: [−231,  231 − 1].

# Analysis

The description of the question expounds on the properties of an ugly number very clearly. An ugly number, except 1, can and can only have 2, 3, and 5 as its prime factors. Then, if we divide an ugly number by 2, 3, and 5 recursively, the result must eventually become 1. 

## Edge case
1. Negative integer: return False directly
2. 0: False
3. 1: True
   
# Implimentation:
We can use the following two method to judge if a given number is an ugly number.
## 1. recursion
```Python
class Solution:
    def isUgly(self, num: int) -> bool:
        if num <= 0:
            return False
        if num == 1:
            return True
        if not num % 2:
            num /= 2
            return self.isUgly(num)
        if not num % 3:
            num /= 3
            return self.isUgly(num)
        if not num % 5:
            num /= 5
            return self.isUgly(num)
        return False
``` 
## 2. while loop
The recursive version is quite clear. However, considering the given number can be very big, the program invokes the recursive call many times, which can be a factor to slow down the program. 

In fact, without much effort, we can change the recursive version to loop version to accelerate the program.

```python
class Solution:
    def isUgly(self, num: int) -> bool:
        if num <= 0:
            return False
        while not num % 2:
            num /= 2
        while not num % 3:
            num /= 3
        while not num % 5:
            num /= 5
        return True if num == 1 else False
```

The previous code does the job, but we can refactor it to make it more pythonic:
```Python
class Solution:
    def isUgly(self, num: int) -> bool:
        if num <= 0:
            return False
        for p in 2, 3, 5:
            while not num % p:
                num /= p
        return True if num == 1 else False
```