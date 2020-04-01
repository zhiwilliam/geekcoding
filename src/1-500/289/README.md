
#### [289. 生命游戏](https://leetcode-cn.com/problems/game-of-life/)

难度**中等**

根据 [百度百科](https://baike.baidu.com/item/%E7%94%9F%E5%91%BD%E6%B8%B8%E6%88%8F/2926434?fr=aladdin) ，生命游戏，简称为生命，是英国数学家约翰·何顿·康威在 1970 年发明的细胞自动机。

给定一个包含 m × n 个格子的面板，每一个格子都可以看成是一个细胞。每个细胞都具有一个初始状态：1 即为活细胞（live），或 0 即为死细胞（dead）。每个细胞与其八个相邻位置（水平，垂直，对角线）的细胞都遵循以下四条生存定律：

1.  如果活细胞周围八个位置的活细胞数少于两个，则该位置活细胞死亡；
2.  如果活细胞周围八个位置有两个或三个活细胞，则该位置活细胞仍然存活；
3.  如果活细胞周围八个位置有超过三个活细胞，则该位置活细胞死亡；
4.  如果死细胞周围正好有三个活细胞，则该位置死细胞复活；

根据当前状态，写一个函数来计算面板上所有细胞的下一个（一次更新后的）状态。下一个状态是通过将上述规则同时应用于当前状态下的每个细胞所形成的，其中细胞的出生和死亡是同时发生的。

**示例：**

**输入：** [
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]
**输出：** [
  [0,0,0],
  [1,0,1],
  [0,1,1],
  [0,1,0]
]

**进阶：**

-   你可以使用原地算法解决本题吗？请注意，面板上所有格子需要同时被更新：你不能先更新某些格子，然后使用它们的更新后的值再更新其他格子。
-   本题中，我们使用二维数组来表示面板。原则上，面板是无限的，但当活细胞侵占了面板边界时会造成问题。你将如何解决这些问题？


### Solution

**思路**

直接换题意，计算每个细胞周围活细胞的个数，再结合当前细胞的状态来更新。

Trick：因为需要同时更新，即前面更新的细胞状态不能影响本次后面细胞状态的更新，所以需要对原状态数组进行复制，保证在更新过程中，仍能引用原状态。这也是**进阶**中提出原地更新的原因。

Trick: 在python中copy()只能对一维数组有效，对二组数组的深度复制，需遍历。
```python
ori = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]

cp1 = ori.copy()  ## deep copy only applied to the first dimention 
id(ori) == id(cp1) ## return False, looks good so far
id(ori[0]) == id(cp1[0])  ## return True, which is not expect

cp2 = [ r.copy() for r in ori]   ### Correct 
id(ori[0]) == id(cp2[0])  ## return False, which is correct 
```
**代码**
非常直接，遍历每一个细胞，计算周围活细胞个数（函数countLive），然后决定是否更新细胞的状态。
```python
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        board_cp = [ row.copy() for row in board ]

        for i in range(len(board)):
            for j in range(len(board[0])):
                liveCt = self.countLive(board_cp, i,j)
                if board[i][j] == 0:
                    if liveCt ==3:
                        board[i][j] = 1 
                    continue 
                # now board[i][j] == 1 
                if liveCt not in [2,3]:
                    board[i][j] = 0

    def countLive(self, board, row, col):
        ct = 0 
        for i in [row -1, row, row+1]:
            if i < 0 or i >= len(board):
                continue 
            for j in [col-1, col, col+1]:
                if j < 0 or j>= len(board[0]):
                    continue 
                if i == row and j == col:
                    continue 
                ct += board[i][j]
        return ct 

```


TBC for the following up question.

