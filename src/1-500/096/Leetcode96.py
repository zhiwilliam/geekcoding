from functools import lru_cache
import math
class Solution:
    @lru_cache(maxsize=32)
    def numTrees(self, n):
        if n <= 1:
            return 1
        res = 0
        for i in range(1, n+1):
            res += self.numTrees(i-1)*self.numTrees(n-i)
        return res

    def numTreesMingAnTu(self, n):
        return int(math.factorial(2*n)/(math.factorial(n+1)*math.factorial(n)))

    def numTreesMingAnTu2(self, n):
        twoN = self.factorial(2*n)
        N1 = self.factorial(n+1)
        N = self.factorial(n)
        return int(twoN/(N1*N))
    @lru_cache(maxsize=32)
    def factorial(self, N):
        if N <= 1:
            return 1
        return N*self.factorial(N-1)

if __name__ == '__main__':
    S = Solution()
    import time
    start = time.time()
    print(S.numTrees(5))
    print(S.numTrees(2))
    print(S.numTrees(3))
    end = time.time()
    print('Method 1 runtime: {} seconds'.format(end-start))
    start = time.time()
    print(S.numTreesMingAnTu(5))
    print(S.numTreesMingAnTu(2))
    print(S.numTreesMingAnTu(3))
    end = time.time()
    print('Method 2 runtime: {} seconds'.format(end-start))
    start = time.time()
    print(S.numTreesMingAnTu2(5))
    print(S.numTreesMingAnTu2(2))
    print(S.numTreesMingAnTu2(3))
    end = time.time()
    print('Method 3 runtime: {} seconds'.format(end-start))
