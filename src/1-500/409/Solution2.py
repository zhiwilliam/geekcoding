class Solution:
    def longestPalindrome(self, s: str) -> int:
        singles = set()
        ret = 0 
        for c in s:
            if c in singles:
                ret += 2 
                singles.discard(c)  # no eoor if c not exist
            else :
                singles.add(c)
        
        return ret + 1 if singles else ret 

