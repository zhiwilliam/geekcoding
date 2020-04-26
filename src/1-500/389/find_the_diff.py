class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        cs, ct = Counter(s), Counter(t)
        for letter in list(ct):
            if (ct[letter] != cs[letter]):
                return letter
        
    def findTheDifference_1(self, s: str, t: str) -> str:
        ss, st = sorted(s), sorted(t)
        for i in range(0, len(st) - 1):
            if ss[i] != st[i]:
                return st[i]
        return st[len(st) - 1]
        
    def findTheDifference_2(self, s: str, t: str) -> str:
        diff = 0
        for c in s:
            ans -= ord(c)
        for c in t:
            ans += ord(c)
        return chr(diff)