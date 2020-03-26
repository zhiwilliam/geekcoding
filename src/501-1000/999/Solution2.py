class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        # find the 'R'
        margin = len(board )
        def findR( ):
            for row in range(len(board)):
                if 'R' in board[row]:
                    return row, board[row].index('R')
            return -1, -1 

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

