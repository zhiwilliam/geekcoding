class Solution:

    # using binary representation, 2^x should be a single 1 followed by all 0's
    def isPowerOfTwo(self, n: int) -> bool:
        binaryString = bin(n)[2:]
        return binaryString[0] == '1' and binaryString.count('1') == 1
    
    # using bit-wise AND, 2^x AND 2^x - 1
    # => 10000... AND 01111... = 00000... = 0
    # unfortunately this contains an edge case of 0, which must be manually excluded
    def isPowerOfTwo_1(self, n: int) -> bool:
        return n != 0 and n & (n-1) == 0
