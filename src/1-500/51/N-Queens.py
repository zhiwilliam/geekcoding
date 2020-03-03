from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def check(k, j):
            for i in range(k):
                if board[i] - j == 0 or k-i == abs(board[i]-j):
                    return False
            return True

        def dfs(depth, valuelist):
            if depth == n: #如果深度和皇后的数目一样了，说明全部皇后都已经摆上棋盘了。
                res.append(valuelist)
                return
            for i in range(n):
                if check(depth, i):
                    board[depth] = i
                    s = '.' * n
                    dfs(depth+1, valuelist + [s[:i]+'Q'+s[i+1:]])
        board=[-1 for i in range(n)] # 把棋盘重构为一直线
        res=[]
        dfs(0,[])
        return res


solution = Solution()
print(solution.solveNQueens(8))
