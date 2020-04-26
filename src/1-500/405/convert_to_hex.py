class Solution:
    def toHex(self, num: int) -> str:
        if num == 0: return '0'
        chars = '0123456789abcdef' # a string that serves as a map of index => hex value for index in 0 ... 15
        result = ''
        i = 0
        while i < 8 and num != 0: # build the result string one character (4 bits) at a time, so for a 32-bit integer we run the loop 8 times
            n = num & 15 # this will get rid of everything but the last 4 bits
            c = chars[n] # this will convert n to its corresponding hex char
            result = c + result # add this hex char to the result, on the left side
            num = num >> 4 # shift the original number to the right by 4 bits so we can process the next number
            i += 1
        return result.lstrip('0')