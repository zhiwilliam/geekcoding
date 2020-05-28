class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        return max(min(abs(house - heater)
            for i in [bisect.bisect(heaters, house)] # binary search to find the closest two heaters
            for heater in heaters[i-(i>0):i+1]) # taking the closer heater among the two closest heaters
            for house in houses) # take the maximum distance to a heater among all houses