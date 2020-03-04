class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle not in haystack: return -1
        if not needle: return 0
        return [i for i in range(len(haystack)) if haystack[i:].startswith(needle)][0]
