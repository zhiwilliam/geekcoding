class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        v = [float('-inf'), float('-inf'), float('-inf')]
        for num in nums:
            if num not in v:
                if num > v[0]:   v = [num, v[0], v[1]]
                elif num > v[1]: v = [v[0], num, v[1]]
                elif num > v[2]: v = [v[0], v[1], num]
        return max(nums) if float('-inf') in v else v[2]