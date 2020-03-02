class Solution:
# My first solution
    def wordPattern(self, pattern: str, str: str) -> bool:
        strs = str.split(' ')
        dict = {}

        if len(pattern) != len(strs):
            return False
        
        if len(set(pattern)) != len(set(strs)):
            return False

        for i in range(0, len(pattern)):
            if (dict.get(pattern[i]) == None):
                dict[pattern[i]] = strs[i]
            elif (dict.get(pattern[i]) != strs[i]):
                return False
        
        return True

# Alternatives (similar runtime/memory performance)
    def wordPattern_1(self, pattern: str, str: str) -> bool:
        s = pattern
        t = str.split()
        return list(map(s.find, s)) == list(map(t.index, t))

    def wordPattern_2(self, pattern: str, str: str) -> bool:
        s = pattern
        t = str.split()
        return len(set(zip(s, t))) == len(set(s)) == len(set(t)) and len(s) == len(t)