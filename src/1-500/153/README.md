# 153. Find Minimum Rotated Sorted Array

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  ***[0,1,2,4,5,6,7]*** might become  ***[4,5,6,7,0,1,2]***).

Find the minimum element.

You may assume no duplicate exists in the array.

## Example 1:

```Python
Input: [3,4,5,1,2] 
Output: 1
```
## Example 2:

```Python
Input: [4,5,6,7,0,1,2]
Output: 0
```

# Analysis:

This question is a typical binary search question. After analyzing the input array, we found the value on the pivot point is the minimum value of the array. Then our task changes to finding the pivot index. Once we get the pivot point, then we can directly return the value on this index.

Example, if our input is:

|index|0|1|2|3|4|5|6|
|---|---|---|---|---|---|---|---|
|value|4|5|6|7|0|1|2|

Followed the boilerplate of binary search, we set the left pointer to 0 and the right one to len(nums)-1, which is 6 for this example.

And the next step is to calulate the middle index of this array.
```Python
left, right = 0, len(nums)-1
mid = left + (right - left) // 2
# For Python2, we can use '/' directly
```
The mid is 3 for this example.
|index|0|1|2|3|4|5|6|
|---|---|---|---|---|---|---|---|
|value|4|5|6|7|0|1|2|
||↑|||↑|||↑|
||l|||m|||r|

We divide the original array into two parts by the middle pointer. By comparing the value on the middle index and the value on left or right, we can find which part contains the pivot point.

1. If nums[mid] > nums[right], this means the right part is not a sorted array, in consequence, the pivot must be in this part. One more thing, because the value on the middle pointer is bigger than the last one on this range, that means the value on the middle index has no way to be the smallest value of the second part. So, we can move the left pointer to the next position to the middle. And we can narrow down the whole searching range to the second part of the array. The following chart shows the new searching area.

    |index|0|1|2|3|4|5|6|
    |---|---|---|---|---|---|---|---|
    |value|4|5|6|7|0|1|2|
    ||||||↑||↑|
    ||||||l||r|

2. If the first condition is not true, that means the second part is a sorted array, and the pivot point must be in the first part. Because we don't know if the value on the middle point is the minimum of the whole array or not, we can only move the right pointer to the middle index and narrow down the searching area to the first part. The following chart illustrates the updated searching area.

    |index|0|1|2|3|4|5|6|
    |---|---|---|---|---|---|---|---|
    |value|4|5|6|0|1|2|3|
    ||↑|||↑||||
    ||l|||r||||

We can keep doing the above operation until we narrow down to the left pointer and right pointer are same, which indicates we've found the minimum value of the array.

# Code snippet:
```Python
class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums:
            return -1
        left, right = 0, len(nums)-1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return nums[left]
```