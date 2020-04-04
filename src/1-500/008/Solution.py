class Solution:
    def myAtoi(self, str: str) -> int:
        if not str:
            return 0 

        INT_MAX = 2**31 - 1 
        INT_MIN = - 2**31 

        ret = 0 
        i = 0
        flag = 1
        max_index = len(str)

        while i< max_index and str[i] == ' ':
            i += 1 
        if i == max_index:
            return 0 
        
        if str[i] not in '+-0123456789':
            return 0  ## not a valid 

        if str[i] in '+-':
            flag = 1 if str[i] == '+' else -1  
            i += 1 
        
        while i < len(str):
            if str[i] not in '0123456789':
                break 
            ret = ret * 10 + ord(str[i]) - ord('0')
            i += 1 
            if ret * flag  >= INT_MAX:
                return INT_MAX 
            if ret * flag <= INT_MIN:
                return INT_MIN 
            
        return ret * flag 


