
### [326. 3的幂](https://leetcode-cn.com/problems/power-of-three/)

难度: **简单**

给定一个整数，写一个函数来判断它是否是 3 的幂次方。

**示例 1:**

**输入:** 27
**输出:** true

**示例 2:**

**输入:** 0
**输出:** false

**示例 3:**

**输入:** 9
**输出:** true

**示例 4:**

**输入:** 45
**输出:** false

**进阶：**  
你能不使用循环或者递归来完成本题吗？ 

### Solution

(1) 持续整除法 
一直把该整数除3，直到该整数小于3。
如果该最后的结束是1，则表明呆以被3整除。
```python
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        while n>=3:
            n = n/3
        
        return n==1
```

执行结果：通过

显示详情
执行用时 :128 ms, 在所有 Python3 提交中击败了22.82%的用户
内存消耗 :13.7 MB, 在所有 Python3 提交中击败了9.09%的用户

(2) 对数法

```python
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        return math.log(n, 3).is_integer()
```
思路很简单，本地运行正常，但在LeetCode环境中运行失败。

```
ValueError: math domain error
    return math.log(n, 3).is_integer()
Line 4 in isPowerOfThree (Solution.py)
    ret = Solution().isPowerOfThree(param_1)
Line 27 in _driver (Solution.py)
    _driver()
Line 40 in <module> (Solution.py)
```
