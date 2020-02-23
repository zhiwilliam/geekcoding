#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#

# @lc code=start


class Solution:
    def numIslands(self, grid) -> int:
        lands = []
        result = 0
        blocks = ((y, x) for y, line in enumerate(grid) for x, i in enumerate(line) if i == "1")

        def detect(r):
            if r[0] >= 0 and r[1] >= 0 and r[0] < len(grid) and r[1] < len(grid[0]):
                if grid[r[0]][r[1]] == "1":
                    lands.append(r)
                    grid[r[0]][r[1]] = "0"

        for b in blocks:
            if(grid[b[0]][b[1]] == "1"):
                grid[b[0]][b[1]] = "0"
                result += 1
                lands.append(b)
                for land in lands:
                    {detect(r) for r in ((land[0]-1, land[1]), (land[0]+1, land[1]), (land[0], land[1]-1), (land[0], land[1]+1))}

        return result

# @lc code=end


if __name__ == "__main__":
    print(Solution().numIslands([
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"],
    ]))

    print(Solution().numIslands([
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "1", "1"],
    ]))
