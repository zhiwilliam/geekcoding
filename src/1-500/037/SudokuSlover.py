class Solution:
    # @param board, a 9x9 2D array
    # Solve the Sudoku by modifying the input board in-place.
    # Do not return any value.

    def solveSudoku(self, board):
        self.board = board
        self.solve()

    def getCandidates(self, row, col):
        board = self.board

        candidates = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

        # remove nums from rows and columns
        for i in range(9):
            if board[row][i] in candidates:
                candidates.remove(board[row][i])
            if board[i][col] in candidates:
                candidates.remove(board[i][col])

        # remove nums from square
        col_start = (col // 3) * 3
        row_start = (row // 3) * 3
        for i in range(row_start, row_start + 3):
            for j in range(col_start, col_start + 3):
                if board[i][j] in candidates:
                    candidates.remove(board[i][j])

        return candidates

    def solve(self):
        board = self.board
        open_squares = []

        # add all open suqares to a list
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    open_squares.append((i, j, self.getCandidates(i, j)))

        # if there are no more open squares, your board is complete
        if not open_squares:
            return True

        # get the open square with the fewest candidates
        open_squares.sort(key=lambda x: len(x[2]))
        a, b, candidates = open_squares[0]

        # try each candidate, and if the board
        # can't be recursively solved, reset to "."
        for can in candidates:
            board[a][b] = can
            if self.solve():
                return True
            board[a][b] = "."

        # if we've gotten here, we've gone down a bad recursive path
        # i.e. all candidates have been tried and there are still open
        # squares, so return False, causing our algo to backtrack.
        return False