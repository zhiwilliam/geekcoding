class Solution:

    # The obvious solution
    def addDigits(self, num: int) -> int:
        newNum = 0
        for digit in [int(c) for c in str(num)]:
            newNum += digit
        if num > 9:
            return self.addDigits(num)
        else:
            return num
    
    # The best solution, feels like a bit of a trivia question.
    def addDigits_1(self, num: int) -> int:
        return num % 9 if num % 9 else 9 if num else 0