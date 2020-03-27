#### [118. 杨辉三角](https://leetcode-cn.com/problems/pascals-triangle/)

难度**简单**

给定一个非负整数 _numRows，_生成杨辉三角的前 _numRows_ 行。

![](https://upload.wikimedia.org/wikipedia/commons/0/0d/PascalTriangleAnimated2.gif)

在杨辉三角中，每个数是它左上方和右上方的数的和。

**示例:**

**输入:** 5
**输出:**
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]

### Solution

直接DP，根据上一行计算下一行。
-初使值：row[0], row[-1] = 1, 1 
-状态转移方程：row[i,j] = row[i-1,j-1] + row[i-1, j], for $\forall j \in (0,i)$ 

代码
```python
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        ret = []
        for i in range(0, numRows):
            row = [ None for _ in range(i+1)]

            row[0], row[-1] = 1, 1 

            for j in range(1,i):
                row[j] = ret[i-1][j-1] + ret[i-1][j]

            ret.append(row)

        return ret 
``` 


