class Solution:
    def reverseWords(self, s: str) -> str:

        #不能用split, trim, stringbuilder, 等function, 只能inplace 修改

        if not s :
            return s 

        words = []
        leftIndex, rightIndex = 0,0
        while leftIndex < len(s):
            while leftIndex < len(s) and  s[leftIndex] == ' ':
                leftIndex += 1 
            if leftIndex == len(s):
                break 
            rightIndex = leftIndex + 1 
            while rightIndex < len(s) and s[rightIndex] != ' ':
                rightIndex += 1 
            
            words.append(s[leftIndex:rightIndex])
            # print('s[{},{}]:"{}"'.format( leftIndex,rightIndex
            #             , s[leftIndex:rightIndex]))
            leftIndex = rightIndex + 1 
        if not words:
            return ''
        ret = words.pop()
        while words:
            w = words.pop()
            ret = ret + ' ' + w 
 
        return ret
