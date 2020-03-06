class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        t = s[::-1]
        return (s == t)
