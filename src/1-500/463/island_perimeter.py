class Solution:
    # def islandPerimeter(self, grid: List[List[int]]) -> int:
    #     p, xmax, ymax = 0, len(grid) - 1, len(grid[0]) - 1
    #     for x in range(0, xmax + 1):
    #         for y in range(0, ymax + 1):
    #             if grid[x][y] == 1:
    #                 q = 0
    #                 if x == 0:
    #                     q += 1
    #                 elif grid[x-1][y] == 0:
    #                     q += 1
    #                 if x == xmax:
    #                     q += 1
    #                 elif grid[x+1][y] == 0:
    #                     q += 1
    #                 if y == 0:
    #                     q += 1
    #                 elif grid[x][y-1] == 0:
    #                     q += 1
    #                 if y == ymax:
    #                     q += 1
    #                 elif grid[x][y+1] == 0:
    #                     q += 1
    #                 p += q
    #     return p
        
        
    def islandPerimeter(self, grid):
        return sum(sum(map(operator.ne, [0] + row, row + [0])) for row in grid + list(map(list, zip(*grid))))
        # a bit of explanation to unpack this solution:
        # list(map(list, zip(*grid))) transposes the 2-D list
        # so grid + list(map(list, zip(*grid))) is a collection of all rows and all columns
        # for each row/column, map(operator.ne, [0] + row, row + [0]) simultaneously compares each element to its left and right neighbor
        # since each pair of different neighbor results in one unit of perimeter, we just sum the number of pairs for all rows and columns