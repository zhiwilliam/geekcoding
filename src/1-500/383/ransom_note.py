class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magList = list(magazine)
        for c in ransomNote:
            if c in magList:
                magList.pop(magList.index(c))
            else:
                return False
        return True
    

    def canConstruct_1(self, ransomNote: str, magazine: str) -> bool:
        mag = Counter(magazine)
        for c in ransomNote:
            if mag[c] == 0:
                return False
            else:
                mag[c] -= 1
        return True

    def canConstruct_2(self, ransomNote: str, magazine: str) -> bool:
        for i in set(ransomNote):
            if ransomNote.count(i) > magazine.count(i):
                return False
        return True