from collections import Counter
from typing import List

class Solution:

    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        c1, c2 = Counter(nums1), Counter(nums2)
        output = []
        for n in set(nums1):
            output.extend([n] * min(c1[n], c2[n]))
        return output

    def intersect_1(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list((Counter(nums1) & Counter(nums2)).elements())