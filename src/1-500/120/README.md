#### [120. 三角形最小路径和](https://leetcode-cn.com/problems/triangle/)

难度**中等**

给定一个三角形，找出自顶向下的最小路径和。每一步只能移动到下一行中相邻的结点上。

例如，给定三角形：

[
     [**2**],
    [**3**,4],
   [6,**5**,7],
  [4,**1**,8,3]
]

自顶向下的最小路径和为 `11`（即，**2** + **3** + **5** + **1** = 11）。

**说明：**

如果你可以只使用  _O_(_n_) 的额外空间（_n_  为三角形的总行数）来解决这个问题，那么你的算法会很加分。

### Solution

典型的动态规划算法：
定义: dp[row,col] 为到目前[row, col]的最小路径和
状态转移方程： dp[row,col] = min( dp[row-1, col-1], dp[row-1, col]) + self.value 
初使值： 对第0列（col=0)，因为没有col-1列，直接取上一行第0列。

**代码**
```python
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # denotes dp[row][col] the minmum path sum for [row][col]
        # then: dp[row][col] = min( dp[row-1][col-1], dp[row-1][col-1]) + triangle[row][col]
        # specific cases for first and last element: 
        #   first element:    dp[row][0] = dp[row-1][0] + triangle[row][0]
        #   last element:     dp[row][row] = dp[row-1][row-1] + triangle[row][row]
        dp = triangle.copy()

        for row in range(1,len(triangle)):
            dp[row][0] = dp[row-1][0] + triangle[row][0]
            for col in range(1, row):
                dp[row][col] = min( dp[row-1][col-1], dp[row-1][col]) + triangle[row][col]

            dp[row][row] = dp[row-1][row-1] + triangle[row][row]
        
        return min( triangle[-1])       
```
**改进**

利用滚动数组可以实现只使用O(n)的额外空间。

**代码**
```python
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # denotes dp[row][col] the minmum path sum for [row][col]
        # then: dp[row][col] = min( dp[row-1][col-1], dp[row-1][col-1]) + triangle[row][col]
        # specific cases for first and last element: 
        #   first element:    dp[row][0] = dp[row-1][0] + triangle[row][0]
        #   last element:     dp[row][row] = dp[row-1][row-1] + triangle[row][row]

        # dp = triangle.copy()
        ct = len(triangle)
        if ct == 1:
            return triangle[0][0]
            
        dp = [ [0]*ct for _ in range(2)]
        dp[0][0] = triangle[0][0]

        for row in range(1,len(triangle)):
            dp_row, dp_pre_row = row%2 , (row-1)%2 

            dp[dp_row][0] = dp[dp_pre_row][0] + triangle[row][0]
            
            for col in range(1, row):
                dp[dp_row][col] = min( dp[dp_pre_row][col-1], dp[dp_pre_row][col]) + triangle[row][col]

            dp[dp_row][row] = dp[dp_pre_row][row-1] + triangle[row][row]
        
        return min( dp[dp_row])

```


