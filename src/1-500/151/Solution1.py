class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        ret = words[::-1]
        return ' '.join(ret)

