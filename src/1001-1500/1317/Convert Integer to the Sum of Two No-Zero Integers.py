class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        for a in range(n):
            if '0'not in f'{a}{n-a}':
                return [a,n-a]
