class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if not (numRows-1):
            return s
        conversion = ""
        for i in range(numRows):
            rowstr = ""
            index = i
            flag = 0
            while (index < len(s)):
                increment = i * 2 if flag else (numRows-i-1) * 2
                rowstr = rowstr + s[index] if increment else rowstr
                index = index + increment
                flag = not flag
            conversion = conversion + rowstr
        return conversion
