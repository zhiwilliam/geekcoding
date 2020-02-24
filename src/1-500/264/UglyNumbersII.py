class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly = [0] * n
        ugly[0] = 1
        i2, i3, i5 = 1, 1, 1
        num2, num3, num5 = 2, 3, 5
        for i in range(1, n):
            ugly[i] = min(num2, num3, num5)
            if ugly[i] == num2:
                num2 = ugly[i2] * 2
                i2 += 1
            if ugly[i] == num3:
                num3 = ugly[i3] * 3
                i3 += 1
            if ugly[i] == num5:
                num5 = ugly[i5] * 5
                i5 += 1
        return ugly[-1]