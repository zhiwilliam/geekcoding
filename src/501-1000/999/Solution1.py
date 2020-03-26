class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        # find the 'R'
        margin = len(board )
        def findR( ):
            for row in range(len(board)):
                if 'R' in board[row]:
                    return row, board[row].index('R')

        # Searching for the 'p' as per direction(dx,dy)
        def catchInDir( x, y, dx, dy):
            x, y = x+dx, y+dy 
            while isValid(x, y):
                if board[x][y] == 'p':
                    return 1 
                x, y = x+dx, y+dy 
            return 0 

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

