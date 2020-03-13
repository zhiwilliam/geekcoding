# class NumArray:    
#     def __init__(self, nums: List[int]):
#         self.sums = []
#         self.sums.append(0)
#         for i in range(0, len(nums)):
#             self.sums.append(self.sums[i] + nums[i])

#     def sumRange(self, i: int, j: int) -> int:
#         return self.sums[j + 1] - self.sums[i]
nums= [1,2,3,4,5,6,7,8]
sums = [sum(nums[:i]) for i in range(1, len(nums) + 1)]
print(sums)