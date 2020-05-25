### [287. 寻找重复数](https://leetcode-cn.com/problems/find-the-duplicate-number/)

难度:**中等**

给定一个包含 _n_  + 1 个整数的数组 _nums_，其数字都在 1 到  _n_ 之间（包括 1 和  _n_），可知至少存在一个重复的整数。假设只有一个重复的整数，找出这个重复的数。

**示例 1:**

**输入:** `[1,3,4,2,2]`
**输出:** 2

**示例 2:**

**输入:** [3,1,3,4,2]
**输出:** 3

**说明：**

1.  **不能**更改原数组（假设数组是只读的）。
2.  只能使用额外的  _O_(1) 的空间。
3.  时间复杂度小于  _O_(_n_<sup>2</sup>) 。
4.  数组中只有一个重复的数字，但它可能不止重复出现一次。

### Solution

因为至少存在一个重复的元素，所以一定有环存在。

两步走：
（1）找出环，用快慢指针，当两者相遇时，一定在环内，因为只有在环内，快指针才可能追上慢指针。
（2）找出环入口（即重复元素），将快指针移到原点（命名为find以避免理解上的混淆）并以与慢指针相同的速度移到，两者再次相遇时就是环入口。

```python
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        slow, fast = nums[0], nums[nums[0]] 
        while slow  != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]

        find = 0
        while find != slow:
            find = nums[find]
            slow = nums[slow]
        
        return find
```

执行结果：通过

执行用时 :80 ms, 在所有 Python3 提交中击败了87.49%的用户
内存消耗 :16.1 MB, 在所有 Python3 提交中击败了35.71%的用户
