from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if len(board) is 0: return
        width = len(board[0]) - 1
        height = len(board) - 1
        def help(x: int, y: int):
            if x < 0 or x > height or y < 0 or y > width:
                return
            if board[x][y] is "O":
                board[x][y] = "g"
                help(x - 1, y)
                help(x, y - 1)
                help(x + 1, y)
                help(x, y + 1)

        for i in range(width + 1):
            if board[0][i] is "O":
                help(0, i)
            if board[height][i] is "O":
                help(height, i)
        for i in range(1, height):
            if board[i][0] is "O":
                help(i, 0)
            if board[i][width] is "O":
                help(i, width)

        print(board)
        for i in range(width + 1):
            for j in range(height + 1):
                if board[j][i] is "O":
                    board[j][i] = "X"
                elif board[j][i] is "g":
                    board[j][i] = "O"

board = [["X","O","X","O","X","O"],
         ["O","X","O","X","O","X"],
         ["X","O","X","O","X","O"],
         ["O","X","O","X","O","X"]]

solution = Solution()
solution.solve(board)
print(board)