class Solution:
    maxint = 2**31-1
    minint = -2**31
    sign = {'+': 1, '-': -1}
    digit = {'0': 0, \
             '1': 1, \
             '2': 2, \
             '3': 3, \
             '4': 4, \
             '5': 5, \
             '6': 6, \
             '7': 7, \
             '8': 8, \
             '9': 9
            }
        
    def subatoi(self, s, sign):
        l = len(s)
        index = 0
        num = 0
        while (index < l and s[index] in self.digit):
            num = num * 10 + self.digit[s[index]]
            if (num*sign > self.maxint):
                return self.maxint
            if (num*sign < self.minint):
                return self.minint
            index += 1
        return num * sign
    
    def myAtoi(self, str: str) -> int:
        str = str.strip(' ')
        if not str:
            return 0
        if str[0] in self.digit:
            return self.subatoi(str, 1)
        elif str[0] in self.sign:
            return self.subatoi(str[1:], self.sign[str[0]])
        else:
            return 0
        
