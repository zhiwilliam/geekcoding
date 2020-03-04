class Solution1:

    def __init__(self):
      self.num_dict = Solution1.num_dict

    num_dict = {
        0: ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"],
        1: ["X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"],
        2: ["C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"],
        3: ["M", "MM", "MMM"]
    }

    def intToRoman(self, num):        
        result = ''
        for i in range(3, -1, -1):
            level = pow(10, i)
            r = num // level
            if r: result += (self.num_dict[i])[r-1]
            num = num % level

        return result

print(Solution1().intToRoman(3099))
#space and readablity over algo
