class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapping = {}
        used = set()
        for i in range(len(s)):
            if s[i] in mapping:
                if t[i] != mapping[s[i]]:
                    return False
            else:
                if t[i] in used:
                    return False 
                mapping[s[i]] = t[i]
                used.add(t[i])
        return True 
