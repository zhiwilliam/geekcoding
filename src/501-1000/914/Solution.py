from typing import List

class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        from collections import Counter
        from functools import reduce
        vals = Counter(deck).values()
        return reduce(self.gcd, vals) >= 2

    def gcd(self, a, b):
        while b:
            a, b = b, a%b
        return a