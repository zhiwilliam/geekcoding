class Solution:
    def reverseVowels(self, s: str) -> str:
        l = list(s)
        i, j = 0, len(s) - 1
        while i < j:
            while (l[i] not in 'aeiouAEIOU' and i < j):
                i += 1
            while (l[j] not in 'aeiouAEIOU' and i < j):
                j -= 1
            l[i], l[j] = l[j], l[i]
            i, j = i + 1, j - 1
        return ''.join(l) 