
#### [999. 车的可用捕获量](https://leetcode-cn.com/problems/available-captures-for-rook/)

难度**简单**

在一个 8 x 8 的棋盘上，有一个白色车（rook）。也可能有空方块，白色的象（bishop）和黑色的卒（pawn）。它们分别以字符 “R”，“.”，“B” 和 “p” 给出。大写字符表示白棋，小写字符表示黑棋。

车按国际象棋中的规则移动：它选择四个基本方向中的一个（北，东，西和南），然后朝那个方向移动，直到它选择停止、到达棋盘的边缘或移动到同一方格来捕获该方格上颜色相反的卒。另外，车不能与其他友方（白色）象进入同一个方格。

返回车能够在一次移动中捕获到的卒的数量。  

**示例 1：**

![](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/02/23/1253_example_1_improved.PNG)

输入：
```
[[".",".",".",".",".",".",".","."]
,[".",".",".","p",".",".",".","."]
,[".",".",".","R",".",".",".","p"]
,[".",".",".",".",".",".",".","."]
,[".",".",".",".",".",".",".","."]
,[".",".",".","p",".",".",".","."]
,[".",".",".",".",".",".",".","."]
,[".",".",".",".",".",".",".","."]]
```
输出：3
解释：
在本例中，车能够捕获所有的卒。

### Solution

**(1)最简单的思路**

先找到车（R），然后按4个方向找卒（p）
- 如果找到，则返回1，
- 否则，比如出界，或遇到像（B），则返回0 

代码：
```python
class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        # find the 'R'
        margin = len(board )
        def findR( ):
            for row in range(len(board)):
                if 'R' in board[row]:
                    return row, board[row].index('R')
            return -1, -1 
        #Catch the p as per direction (dx, dy)
        def catchInDir( x, y, dx, dy):
            x, y = x+dx, y+dy 
            while isValid(x, y):
                if board[x][y] == 'p':
                    return 1 
                x, y = x+dx, y+dy 
            return 0 
        #是否出界或同到像R
        def isValid(x, y):
            if x < 0 or y < 0:
                return False 
            if x >= margin or y>= margin:
                return False 
            if board[x][y] == 'B':
                return False 
            return True 
        
        dirs = ( (-1, 0), (1, 0), (0, -1), (0, 1))
        x, y = findR()
        ret = 0 
        for dx, dy  in dirs:
            ret += catchInDir(x, y, dx, dy )

        return ret 
```
问题： 效率低
行用时 :48 ms, 在所有  Python3  提交中击败了24.49%的用户
内存消耗 :13.6 MB, 在所有  Python3  提交中击败了5.26%的用户

**(2)优化，从dx 和 dy两个方向分别实现**
方法（1）中，dx,dy只能有一个为非负，所以可以分开写，提高点效率

```python
class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        # find the 'R'
        margin = len(board )
        def findR( ):
            for row in range(len(board)):
                if 'R' in board[row]:
                    return row, board[row].index('R')
            return -1, -1 
        # Searching in X direction
        def catchInDirX( x, y, dir):
            while 0<= x < margin and board[x][y] != 'B':
                if board[x][y] == 'p':
                    return 1 
                x += dir 
            return 0              

        def catchInDirY( x, y, dir):
            while 0<= y < margin and board[x][y] != 'B':
                if board[x][y] == 'p':
                    return 1 
                y += dir 
            return 0

        dirs = ( -1, 1 )
        x, y = findR()
        ret = 0 
        for dir  in dirs:
            ret += catchInDirX(x, y, dir)
            ret += catchInDirY(x, y, dir)

        return ret 
```

执行用时 :36 ms, 在所有  Python3  提交中击败了60.20%的用户
内存消耗 :13.8 MB, 在所有  Python3  提交中击败了5.26%的用户


**(3) 从X方向查找可以利用List的 in 和 index 操作**

实验结果表明，速度并没有提高，或者说在小数据集下性能无差异


