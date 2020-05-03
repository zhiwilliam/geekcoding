class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        c1, c2 = 0, 0
        while c1 < len(g) and c2 < len(s):
            if g[c1] <= s[c2]:
                c1 += 1
            c2 += 1
        return c1