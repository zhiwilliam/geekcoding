class Solution:
    def generateParenthesis(self, n):
        def generate(n, open_par=0):
            if n > 0 <= open_par:
                return ['(' + par for par in generate(n-1, open_par+1)] + \
                       [')' + par for par in generate(n, open_par-1)]
            return [')' * open_par] * (not n)
        return generate(n)

if __name__ == '__main__':
   S = Solution()
   result = S.generateParenthesis(4)
   print(result)
   print(len(result))
