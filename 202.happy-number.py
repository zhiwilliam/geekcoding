#
# @lc app=leetcode id=202 lang=python3
#
# [202] Happy Number
#
# Too easy to say...

# @lc code=start


class Solution:
    def isHappy(self, n: int) -> bool:
        history = set()
        while n != 1:
            stack = []
            while n > 0:
                x = n % 10
                p = pow(x, 2)
                stack.append(p)
                n = n // 10
            n = sum(stack)
            if(history.__contains__(n)):
                return False
            else:
                history.add(n)
        return True


if (__name__ == "__main__"):
    print(Solution().isHappy(19))

# @lc code=end
