class Solution:
    def isUgly_recur(self, num: int) -> bool:
        if num <= 0:
            return False
        if num == 1:
            return True
        if not num % 2:
            num /= 2
            return self.isUgly(num)
        if not num % 3:
            num /= 3
            return self.isUgly(num)
        if not num % 5:
            num /= 5
            return self.isUgly(num)
        return False

    def isUgly(self, num: int) -> bool:
        if num <= 0:
            return False
        while not num % 2:
            num /= 2
        while not num % 3:
            num /= 3
        while not num % 5:
            num /= 5
        return True if num == 1 else False

    def isUgly1(self, num: int) -> bool:
        if num <= 0:
            return False
        for p in 2, 3, 5:
            while not num % p:
                num /= p
        return True if num == 1 else False