class Solution:
    def findComplement(self, num: int) -> int:
        return (2 ** (len(bin(num))-2) - 1) ^ num