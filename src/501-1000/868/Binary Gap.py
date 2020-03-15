class Solution:
    def binaryGap(self, N: int) -> int:
            #def binaryGap(self, N):
        index = [i for i, v in enumerate(bin(N)) if v == '1']
        return max([b - a for a, b in zip(index, index[1:])] or [0])
