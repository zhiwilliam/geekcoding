class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        def helper(n, k, cur, tmp = []):
            if len(tmp) == k:
                result.append(tmp[:])
                return
            for i in range(cur, n):
                tmp.append(i + 1)
                helper(n, k, i + 1, tmp)
                tmp.pop()
            return

        helper(n, k, 0)
        return result