class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        size = len(strs)
        if size == 0:
            return ""
        if size == 1:
            return strs[0]
        strs.sort()
        print(strs)
        end = min([len(s) for s in strs])
        i = 0
        while i < end and strs[0][i] == strs[size - 1][i]:
            i += 1
        return strs[0][0: i] 