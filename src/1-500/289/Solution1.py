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

