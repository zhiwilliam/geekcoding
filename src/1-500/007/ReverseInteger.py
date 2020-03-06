class Solution:
    def reverse(self, x: int) -> int:
        sign = 1 if x >= 0 else -1
        y = x * sign
        z = str(y)
        z = z[::-1]
        z = int(z) * sign
        if (z < 2**31-1 and z > -2**31):
            return z
        else:
            return 0
        
