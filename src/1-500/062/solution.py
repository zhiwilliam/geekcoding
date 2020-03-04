class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        path_map = {}
        for i in range(m):
            for j in range(n):
                if i not in path_map:
                    path_map[i] = {}
                # if first row or first column
                if i == 0 or j == 0:
                    path_map[i][j] = 1
                # else, current number is equal to the sum of upper column + left column
                else:
                    path_map[i][j] = path_map[i-1][j] + path_map[i][j-1]
                    
        return path_map[m-1][n-1]

