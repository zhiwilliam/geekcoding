class Solution:
    def titleToNumber(self, s: str) -> int:
        length, res = len(s), 0
        for ch in s:
            length -= 1
            res += (ord(ch) - ord('A') + 1) * 26 ** length  # 26-based
        return res
