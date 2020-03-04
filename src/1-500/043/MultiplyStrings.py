class Solution(object):
    def multiply(self, num1, num2):
        res = [0] * (len(num1) + len(num2))  # 初始化，存放乘积的数组
        pos = len(res) - 1

        for n1 in num1[::-1]:
            tempPos = pos
            for n2 in num2[::-1]:
                res[tempPos] += int(n1) * int(n2)
                res[tempPos - 1] += res[tempPos] // 10  # 进位
                res[tempPos] %= 10  # 取余
                tempPos -= 1
            pos -= 1

        st = 0
        while st < len(res) - 1 and res[st] == 0:  # 统计前面有几个0
            st += 1
        return ''.join(map(str, res[st:]))  # 去掉0，然后变成字符串，并返回


solution = Solution()
print(solution.multiply("89", "67"))