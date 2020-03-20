# 题目
Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Note:

Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.
Follow up:

What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is better?
What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?

# 级别 
Easy

# 算法口号
Using Counters/dictionaries provides solutions in O(m+n) time

# 解题思路
The problem can be solved fairly easily by using collections.Counter to count the appearances of each value in each list. Iterating over the keys of one counter and taking the lesser count for the same key in each counter gives the number of times the key appears in both lists.  

Alternatively, the Counter class provides a way to calculate the intersection directly.

Time Complexity: O(m+n) since building each counter is O(n) and iterating through it is also O(n)
Space Complexity: O(m+n)

**Follow up questions:**
- if the arrays are already sorted, we can use two pointersto iterate both of them, advancing the pointer with the lesser value each time, and advancing both pointers when the values are equal while appending the value to output. This is also O(m+n) time and space.
- if num1's size is smaller than num2, we can still apply the original solution using Counters/dictionaries. If the input follows specific patterns (num1's range is much smaller than num2, both arrays are sorted, etc.), further optimization should be possible (removing out-of-range values in num2, doing a search in num2 for each item in num1, etc.)
- if one or both arrays are too big to fit in memory, we can load them in chucks to build the two Counters. However, if the values in each array are so diverse such that the Counter cannot fit into memory, then I don't know if this can be done without actively writing to the disk...
