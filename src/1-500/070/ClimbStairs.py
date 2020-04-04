class Solution:

    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        first, second = 1, 2
        for i in range(3, n + 1):
            third = first + second
            first = second
            second = third
        return second

solution = Solution()
print(solution.climbStairs(10))