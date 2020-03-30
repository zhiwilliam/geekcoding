#### [119. 杨辉三角 II](https://leetcode-cn.com/problems/pascals-triangle-ii/)

难度**简单**

给定一个非负索引 _k_，其中  _k_ ≤ 33，返回杨辉三角的第  _k_ 行。

![](https://upload.wikimedia.org/wikipedia/commons/0/0d/PascalTriangleAnimated2.gif)

在杨辉三角中，每个数是它左上方和右上方的数的和。

**示例:**

**输入:** 3
**输出:** [1,3,3,1]

**进阶：**

你可以优化你的算法到  _O_(_k_) 空间复杂度吗？

### Solution

直接利用Leet118的动态规划解法，然后得出第k行即可。

进阶：利用滚动数组来节省空间，因为始终只有上一行有用，再之前的数据就可以丢弃了。


**Tips**
第_k_行是从0开始的，故在生成dp和LOOP时，均需+1，否则会输出第_k-1_行


### 代码
```python
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        #dp, denotes dp[row][col] = dp[row-1][col-1] + dp[row-1][col] for col >= 1, row >= 1 
        #dp, dp[row][0] = 1 , dp[row][row] = 1
        dp = [ [1] * (rowIndex+1) for _ in range(2)]

        for i in range(1,rowIndex+1):
            for j in range(1, i ): 
                dp[i%2][j] = dp[(i -1)%2][j-1] + dp[(i-1)%2][j]

        return dp[i%2]
```

