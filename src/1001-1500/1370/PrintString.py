class Solution:
    # assumes: All characters are lower cases.
    def sortString(self, s: str) -> str:
        strlen = len(s)
        if strlen == 0: return ""
        asciia = ord('a')
        dp = [0 for i in range(26)]
        for character in s:
            dp[ord(character) - asciia] += 1
        hasValue = True  # because string length > 0
        start, end, direction = 0, 26, 1
        returnList = [' ' for _ in range(strlen)]
        strIndex = 0
        while hasValue:
            hasValue = False
            for index in range(start, end, direction):
                if dp[index] > 0:
                    hasValue = True
                    returnList[strIndex] = chr(index + asciia)
                    strIndex += 1
                    dp[index] -= 1
            if start == 0:
                start, end, direction = 25, -1, -1
            else:
                start, end, direction = 0, 26, 1

        return ''.join([char for char in returnList])


solution = Solution()
print(solution.sortString("aaaabbbbcccc"))