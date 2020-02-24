class Solution:
    def singleNumber(self, nums):
        if nums == []:
            return
        visited = {}
        for num in nums:
            if num not in visited:
                visited[num] = 0
            else:
                del visited[num]
        result = list(visited.keys())
        return result[0]