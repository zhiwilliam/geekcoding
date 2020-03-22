class Solution:
    def bitwiseComplement(self, N: int) -> int:

        return (1 << len(bin(N)) >> 2) - N - 1
