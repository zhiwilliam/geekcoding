class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        res = [None] * (m + n)
        i = 0
        j = 0
        k = 0

        while i < m and j < n:
            if nums1[i] < nums2[j]:
                res[k] = nums1[i]
                i += 1
                k += 1
            else:
                res[k] = nums2[j]
                j += 1
                k += 1

        # if nums1 has unfinish elements
        while i < n:
            res[k] = nums1[i]
            k += 1
            i += 1

        # same for nums2
        while j < n:
            res[k] = nums2[j]
            k += 1
            j += 1

        for i in range(m + n):
            nums1[i] = result[i]
