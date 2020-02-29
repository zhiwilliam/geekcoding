class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d = {}
        for idx in range(len(nums)):
            n = nums[idx]
            if n in d:
                if idx - d[n] <= k:
                    return True
                else:
                    d[n] = idx 
            else:
                d[n] = idx 
        return False 
