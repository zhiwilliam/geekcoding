class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        if s1 is None or s2 is None or len(s1) != len(s2):
            return False

        Len= len(s1)
        if Len == 1:
            return s1 == s2
        else: 
            for i in range(1, Len):
                s1_left = s1[:i]
                s1_right = s1[i:]
                s2_left = s2[:-i]
                s2_right = s2[-i:]
            
                if self.isScramble(s1_left, s2_right) and self.isScramble(s1_right, s2_left):
                    return True
                
                s2_left = s2[:i]
                s2_right = s2[i:]
                if self.isScramble(s1_left, s2_left) and self.isScramble(s1_right, s2_right):
                    return True
            return False