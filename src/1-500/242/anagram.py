class Solution:
    # keep count of each letter of first string in a dictionary
    # decrement the count whenever the letter shows up in second string
    # if every letter in one string corresponds to one in the other string, all counts should be zero
    # that's when we know they are anagrams
    # O(n) time since dictionary's get and set are O(1)
    # O(1) space since there's an upper-bound on the dictionary's size, assuming the number of letters are finite
    def isAnagram(self, s: str, t: str) -> bool:
        d = {}
        for letter in s:
            if letter not in d:
                d[letter] = 1
            else:
                d[letter] += 1
        for letter in t:
            if letter not in d:
                return False
            else:
                d[letter] -= 1
        for val in d.values():
            if val != 0:
                return False
        return True

    
    # sort the strings first, which makes the function O(n log n) time and O(1) space in general
    # however in this specific scenario it's O(n) space since sorted() creates a character array from the string
    def isAnagram_1(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)