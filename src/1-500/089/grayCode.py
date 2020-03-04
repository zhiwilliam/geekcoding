class Solution:
    def grayCode(self, n: int) -> List[int]:
        arr = list()

        # From WIKI how binary transfer to GRAY CODE
        #   unsigned int BinaryToGray(unsigned int num)
        #       {
        #           return num ^ (num >> 1);
        #       }

        for i in range(1 << n):
            arr.append(i ^ (i >> 1))
        return arr