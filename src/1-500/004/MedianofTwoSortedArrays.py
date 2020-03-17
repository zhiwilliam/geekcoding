from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        index1 = 0
        index2 = 0
        mergedArr = []
        while index1 < len(nums1) and index2 < len(nums2):
            if nums1[index1] > nums2[index2]:
                mergedArr.append(nums2[index2])
                index2 += 1
            elif nums1[index1] < nums2[index2]:
                mergedArr.append(nums1[index1])
                index1 += 1
            else:  # equal
                mergedArr.append(nums1[index1])
                mergedArr.append(nums2[index2])
                index1 += 1
                index2 += 1

        if index1 != len(nums1):
            while index1 < len(nums1):
                mergedArr.append(nums1[index1])
                index1 += 1

        if index2 != len(nums2):
            while index2 < len(nums2):
                mergedArr.append(nums2[index2])
                index2 += 1

        mergedLen = len(mergedArr)
        if mergedLen % 2 == 0:  # even length
            return float(mergedArr[mergedLen // 2] + mergedArr[mergedLen // 2 - 1]) / 2
        else:
            return float(mergedArr[(mergedLen - 1) // 2])

solution = Solution()
print(solution.findMedianSortedArrays([1, 3], [2]))