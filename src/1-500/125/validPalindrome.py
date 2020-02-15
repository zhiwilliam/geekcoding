class Solution:
    def isPalindrome(self, s):
        cleanlist = [c for c in s.lower() if c.isalnum()]
        return cleanlist == cleanlist[::-1]


solution = Solution()
solution.isPalindrome("a b c,d")