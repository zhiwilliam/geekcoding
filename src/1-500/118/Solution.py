class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        ret = []
        for i in range(0, numRows):
            row = [ None for _ in range(i+1)]

            row[0], row[-1] = 1, 1 

            for j in range(1,i):
                row[j] = ret[i-1][j-1] + ret[i-1][j]

            ret.append(row)

        return ret 

