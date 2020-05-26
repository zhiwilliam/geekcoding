
### [152. 乘积最大子数组](https://leetcode-cn.com/problems/maximum-product-subarray/)

难度:**中等**

给你一个整数数组  `nums` ，请你找出数组中乘积最大的连续子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。

**示例 1:**

**输入:** [2,3,-2,4]
**输出:** `6`
**解释:** 子数组 [2,3] 有最大乘积 6。

**示例 2:**

**输入:** [-2,0,-1]
**输出:** 0
**解释:** 结果不能为 2, 因为 [-2,-1] 不是子数组。

### Solution

典型的动态规划题

Tips：
（1）考虑到负数的影响，需同时维护最大和最小两个状态函数。
（2）由于每个状态只依赖于前一个状态，所以可以用滚动数组来节省空间复杂度。

**Code #1** 未使用滚动数组, 时间复杂度和空间复杂度均为O(n):
```python
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        fmax, fmin = nums.copy(), nums.copy()

        for index in range(1, len(nums)):
            num = nums[index]
            pre_index = index - 1 
            fmax[index] = max( fmax[pre_index] * num, fmin[pre_index]*num, num  )
            fmin[index] = min( fmax[pre_index] * num, fmin[pre_index]*num, num  )

        return max(fmax)

执行结果：通过

执行用时 :44 ms, 在所有 Python3 提交中击败了92.88%的用户
内存消耗 :15.1 MB, 在所有 Python3 提交中击败了12.50%的用户
```


**Code #2**  使用滚动数组，时间复杂度不变，仍为O(n)，但空间复杂度除为O(1) 
```python
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        fmax, fmin = [ nums[0]]*2, [nums[0]]*2
        ret = nums[0]
        for index in range(1, len(nums)):
            pre_index = (index - 1)%2
            num = nums[index]
            fmax[index%2] = max( fmax[pre_index] * num, fmin[pre_index]*num, num  )
            fmin[index%2] = min( fmax[pre_index] * num, fmin[pre_index]*num, num  )
            ret = max(max(fmax), ret )
        return ret 

执行结果：通过

执行用时 :52 ms, 在所有 Python3 提交中击败了68.43%的用户
内存消耗 :13.6 MB, 在所有 Python3 提交中击败了25.00%的用户
```

