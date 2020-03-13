class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        return num != 0 and num & (num-1) == 0 and len(bin(num)[2:]) % 2 == 1