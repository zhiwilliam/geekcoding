# 688. Knight Probability in Chessboard
On an NxN chessboard, a knight starts at the r-th row and c-th column and attempts to make exactly K moves. The rows and columns are 0 indexed, so the top-left square is (0, 0), and the bottom-right square is (N-1, N-1).

A chess knight has 8 possible moves it can make, as illustrated below. Each move is two squares in a cardinal direction, then one square in an orthogonal direction.

Each time the knight is to move, it chooses one of eight possible moves uniformly at random (even if the piece would go off the chessboard) and moves there.

The knight continues moving until it has made exactly K moves or has moved off the chessboard. Return the probability that the knight remains on the board after it has stopped moving.

 

## Example:


Input: 3, 2, 0, 0

Output: 0.0625

### Explanation:
 There are two moves (to (1,2), (2,1)) that will keep the knight on the board.
From each of those positions, there are also two moves that will keep the knight on the board.
The total probability the knight stays on the board is 0.0625.
 

### Note:

* N will be between 1 and 25.
* K will be between 0 and 100.
* The knight always initially starts on the board.

# 分析：
这是一道动态规划题。我试着用BFS来解这道题，虽然答案对，但是超时了。所以本题还是要用DP的方法来做。我们用一个二维数组，dp[x][y], 来表示第K步之后knight落在这一个棋盘格上的概率。所以最终的结果是将这个二维数组中的所有的数字累加。