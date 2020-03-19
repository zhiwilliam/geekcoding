class Solution:
    def longestPalindrome(self, s: str) -> int:
        ct = {c:0 for c in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'}
        for c in s:
            ct[c] += 1 
        ans = 0 
        flag = 0
        for _, n in ct.items():
            if n%2 ==0:
                ans += n 
            else:
                ans += n - 1 
                flag = 1 

        return ans + flag 
