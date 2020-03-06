class Solution:
    def numberOfSteps (self, num: int) -> int:
        return(sum([1 for i in bin(num) if i=='1'])+len(bin(num))-3)
        
        
        
        
