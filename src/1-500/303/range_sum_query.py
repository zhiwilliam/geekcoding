class NumArray:    
    def __init__(self, nums: List[int]):
        self.sums = []
        self.sums.append(0)
        for i in range(0, len(nums)):
            self.sums.append(self.sums[i] + nums[i])

    def sumRange(self, i: int, j: int) -> int:
        return self.sums[j + 1] - self.sums[i]