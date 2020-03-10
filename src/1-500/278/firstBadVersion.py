# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):
import math

class Solution:
    def firstBadVersion(self, n):
        lowerBound, upperBound = 1, n
        while lowerBound != upperBound:
            print (upperBound, lowerBound)
            middle = math.floor(lowerBound + (upperBound - lowerBound) / 2)
            if isBadVersion(middle):
                upperBound = middle
            else:
                lowerBound = middle + 1
        return lowerBound