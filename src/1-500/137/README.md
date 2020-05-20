

#### [137. 只出现一次的数字 II](https://leetcode-cn.com/problems/single-number-ii/)

难度 中等

给定一个**非空**整数数组，除了某个元素只出现一次以外，其余每个元素均出现了三次。找出那个只出现了一次的元素。

**说明：**

你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？

**示例 1:**

**输入:** [2,2,3,2]
**输出:** 3

**示例 2:**

**输入:** [0,1,0,1,0,1,99]
**输出:** 99

### Solution

#### （1）简单算术

由于只有一个例外，其他都是出现3次，则可以通过集合运算得到每个数，再通过简单的算术运算求出这个例外的数。

例如，数组A： [ a, a, b, b, c, c, d, a, b, c]，答案为d，满足：

3*（a+b+c+d) - sum(A) = 2*d 

code
```python
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        elements = set(nums)
        
        return (3*sum(elements) - sum(nums) )//2

```
