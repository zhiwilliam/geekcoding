class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for i in range(0, len(s) // 2):
            s[i], s[len(s) - 1 - i] = s[len(s) - 1 - i], s[i]
            

        """
        One-liners, probably unsuitable for interviews
        """
        # s.reverse()

        # s[:] = s[::-1]