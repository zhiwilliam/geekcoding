class Solution:
    def ispalindromic(self, i, j):
        s = self.string
        l = len(s)
        forstr = s[i:j+1]
        backstr = self.reverse[l-j-1:l-i]
        if (forstr == backstr):
            return 1
        else:
            return 0
    
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        sdict = {}
        self.reverse = ""
        self.string = s
        longest = s[0]
        longestlen = 1
        l = len(s)
        for i in range(l):
            self.reverse = s[i] + self.reverse
            if s[i] in sdict:
                sdict[s[i]].append(i)
            else:
                sdict[s[i]] = [i]
        print(sdict)
        print(self.reverse)
        for key in sdict:
            charlist = sdict[key]
            lc = len(charlist)
            if charlist[-1]-charlist[0]+1 <= longestlen:
                continue
            for i in range(lc):
                ci = charlist[i]
                if charlist[-1]-ci+1 <= longestlen:
                    continue
                for j in range(i+1, lc):
                    cj = charlist[j]
                    if cj-ci+1 <= longestlen:
                        continue
                    if self.ispalindromic(ci, cj):
                        longest = s[ci:cj+1]
                        longestlen = len(longest)
        return longest
        
