class Solution:
    def countPrimes(self, n: int) -> int:
        res = [1]*n 
        res[:2] = [0,0] 
        # print(res)
        base = 2
        while base*base  < n+1:
            if res[base] == 1:
                multiplier=base*base 
                while multiplier < n:
                    res[multiplier]= 0
                    multiplier += base 
                # print(base, multiplier, res )
            base += 1 

        # print(res)
        return sum(res)  

