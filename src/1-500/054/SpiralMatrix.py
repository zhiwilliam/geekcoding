from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # 检查matrix合法
        if not matrix or not matrix[0]: return []
        M, N = len(matrix), len(matrix[0])
        # 定义四个边界
        left, right, up, down = 0, N - 1, 0, M - 1
        res = []
        x, y = 0, 0
        # 定义四个方向，从而使处理变得统一
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        cur_d = 0
        while len(res) != M * N:
            res.append(matrix[x][y])
            # 状态机，对边界进行处理。
            if cur_d == 0 and y == right:
                cur_d += 1
                up += 1
            elif cur_d == 1 and x == down:
                cur_d += 1
                right -= 1
            elif cur_d == 2 and y == left:
                cur_d += 1
                down -= 1
            elif cur_d == 3 and x == up:
                cur_d += 1
                left += 1
            cur_d %= 4
            x += dirs[cur_d][0]
            y += dirs[cur_d][1]
        return res


solution = Solution()
input = [
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]

print(solution.spiralOrder(input))