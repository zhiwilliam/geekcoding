# Missing number

Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

## Example 1:
```
Input: [3,0,1]
Output: 2
```
## Example 2:
```
Input: [9,6,4,2,3,5,7,0,1]
Output: 8
```
## Note:
Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?

# Analysis
We can use three methods to solve this question:
1. Brute force
2. Bit operate
3. Gauss's formula

## Method 1: brute force
This method is quite straightforward. We loop through from 0 to n (length of input array plus 1) and keep checking if the current index exists in the input array. 

The code performs:
```Python
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # This is not duplication in nums, to accelerate the search, we use set.
        nums_set = set(nums)
        for i in range(len(nums)+1):
            if i not in nums_set:
                return i    
        return -1
```
* Space complexity: <span style="color:red">***O(n)***</span>
* time complexity: <span style="color:red">***O(n)***</span>

## Method 2: bit operation
Before using this method, let's analyze the features of the input array. There are 2 features of it:
1. There is only one missing number
2. The n distinct numbers are taken from the range from 0 to (n+1).

Let use the first example in the description part to analysis:
```Python
nums = [3, 0, 1]
```
The length of the array is 3, and the 3 distinct numbers are taken from the first 4 natural numbers. Because the length of the array is 3, if there is no missing number from 0, 1, and 2, then the 3 cannot show up in the array. Then we can easily draw a conclusion that 3 must take place someone else. We can use xor operator to solve this question.
|index|0|1|2|
|:----|:----:|:----:|:----:|
|value|3|0|1|
The equation is:
```Python
result = 3 ^ (0^3)^(1^0)^(2^1)
# We can rearrange the order of the numbers in the above equation because the xor operation is associative
       = (3^3)^(0^0)^(1^1)^2
       = 0^0^0^2
       = 2
```
The code is:
```Python
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res =  len(nums)
        for idx, value in enumerate(nums):
            res ^= idx ^ value
        return res
```
* Space complexity: <span style="color:red">***O(n)***</span>
* time complexity: <span style="color:red">***O(1)***</span>

## Method 3:
We know the n distinct numbers are chosen from the first n+1 nutural numbers. And there is only one missing number. Then it is not difficult to find the difference of frist (n+1) nutural numbers and the sum of input array is the missing number.

The code is:
```Python
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums) + 1
        return n*(n-1)//2 - sum(nums)
```
* Space complexity: <span style="color:red">***O(1)***</span>
* time complexity: <span style="color:red">***O(1)***</span>