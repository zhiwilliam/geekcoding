class Solution:
    def maxDepthAfterSplit(self, seq: str) -> List[int]:

        ret = [0]*len(seq)

        for i,c  in enumerate(seq):
            if c =='(':
                ret[i] = i%2 
            else:
                ret[i] = 1 - i%2 
        return ret
