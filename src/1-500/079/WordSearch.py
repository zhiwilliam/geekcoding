from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def exit(x: int, y: int, i: int):
            if i == len(word):
                return True
            if x < 0 or x >= len(board[0]) or y < 0 or y >= len(board):
                return False
            # 检查当前值是否符合条件
            if board[y][x] != word[i]:
                return False
            board[y][x] = board[y][x].swapcase()
            isexit = exit(x + 1, y, i + 1) or exit(x, y + 1, i + 1) or exit(
                x - 1, y, i + 1) or exit(x, y - 1, i + 1)
            board[y][x] = board[y][x].swapcase()
            return isexit

        for y in range(len(board)):
            for x in range(len(board[0])):
                if exit(x, y, 0):
                    return True
        return False



solution = Solution()
print(solution.exist([['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']], "ABCCED"))