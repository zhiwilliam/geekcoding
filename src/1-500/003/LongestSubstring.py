class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dict = {}
        start, res, i = 0, 0, -1
        for i, c in enumerate(s):
            if c in dict and dict[c] >= start:
                res = max(i - start, res)
                start = dict[c] + 1
            dict[c] = i
        return max(i - start + 1, res)


solution = Solution()
print(solution.lengthOfLongestSubstring("d"))

