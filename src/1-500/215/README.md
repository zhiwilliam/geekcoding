# 215. Kth Largest Element in an Array
Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

## Example 1:
```Python

Input: [3,2,1,5,6,4] and k = 2
Output: 5
```
## Example 2:
``` Python

Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4
```

## Note:
You may assume k is always valid, 1 ≤ k ≤ array's length.

# Approach 1: built-in method
This method won't make interviewers happy. We can think this method is a bottom-line. When you run out of idea, at lease you can use the Python list's built-in behaviors to do something, ***better than nothing!***
## code:
```Python
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort(reverse=True)
        return nums[k-1]
```
* time complexity: ***O(nlogn)***
* space complexity: ***O(1)***

## note:
You are not suggested to use the sorted function to sort the input list. The sorted function doesn't sort the list in-place. The consequence is that the space complexity becomes ***O(n)***

# Approach 2: Priority Queue
```Python
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import heapq
        queue = []
        res = None
        for num in nums:
            heapq.heappush(queue, -num)
        while k:
            res = heapq.heappop(queue)
            k -= 1
        return -res
```

* time complexity: O(nlogn + logk)
* space complexity: O(n)