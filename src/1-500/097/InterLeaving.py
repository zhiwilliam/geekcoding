class Solution:
    def helper(self, s1: str, s2: str, s3: str, p1: int, p2: int, p3: int):
        if p1 < 0 and p1 < 0 and p3 < 0:
            return True

        # base case for pointers
        if p3 < 0 and (p1 >= 0 or p2 >= 0):
            return False

        if (p1, p2) not in self.memo:

            ans = False

            if s1[p1] == s2[p2]:
                if s1[p1] == s3[p3]:

                    path1 = False
                    path2 = False

                    if p1 >= 0:
                        path1 = self.helper(s1, s2, s3, p1 - 1, p2, p3 - 1)

                    if p2 >= 0:
                        path2 = self.helper(s1, s2, s3, p1, p2 - 1, p3 - 1)

                    ans = path1 or path2
                else:
                    ans = False
            else:
                if s1[p1] == s3[p3]:
                    ans = self.helper(s1, s2, s3, p1 - 1, p2, p3 - 1)
                elif s2[p2] == s3[p3]:
                    ans = self.helper(s1, s2, s3, p1, p2 - 1, p3 - 1)
                else:
                    ans = False

            self.memo[(p1, p2)] = ans

        return self.memo[(p1, p2)]

    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if (len(s1) + len(s2)) != len(s3):
            return False

        if len(s1) == 0:
            return s2 == s3
        if len(s2) == 0:
            return s1 == s3

        self.memo = {}

        p1, p2, p3 = len(s1) - 1, len(s2) - 1, len(s3) - 1
        return self.helper(s1, s2, s3, p1, p2, p3)


solution = Solution()
print(solution.isInterleave("aabcc", "dbbca", "aadbbcbcac"))