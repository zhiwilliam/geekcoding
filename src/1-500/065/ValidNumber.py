class Solution:
    def isNumber(self, s: str) -> bool:
        i, k, length = 0, 0, len(s)
        # trim
        while i < length and s[i] == ' ': i += 1
        if i < length and (s[i] == '+' or s[i] == '-'): i += 1
        while i < length and s[i].isdigit():
            i += 1
            k += 1
        if i < length and s[i] == '.': i += 1
        while i < length and s[i].isdigit():
            i += 1
            k += 1
        if k == 0: return False
        if i < length and s[i] == 'e':
            i += 1
            k = 0
            if i < length and (s[i] == '+' or s[i] == '-'):
                i += 1
            while i < length and s[i].isdigit():
                i += 1
                k += 1
            if k == 0:
                return False
        while i < length and s[i] == ' ':
            i += 1
        return i == length


solution = Solution()
print(solution.isNumber("-213.2e+33"))