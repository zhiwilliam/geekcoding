class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return s and (s+s)[1:-1].find(s) != -1