import functools 

class Solution1:

    def __init__(self):
      self.roman_dict = Solution1.roman_dict

    roman_dict = {
        "M":1000,
        "D":500,
        "C":100,
        "L":50,
        "X":10,
        "V":5,
        "I":1
    }

    def romanToInt(self, roman): 
        result = 0
        prev = 4000 
        for i in [self.roman_dict[c] for c in list(roman)]:
            if prev < i:
                result += i - 2 * prev 
            else:
                result += i
            prev = i
        return result

print(Solution1().romanToInt("MMMXCIX"))

