import operator
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}
        ret = []
        for x in tokens:
            if x not in ops:
                ret.append(x)
            else:
                op1 = ret.pop()
                op2 = ret.pop()
                ret.append(int(ops[x](int(op2), int(op1))))
        return int(ret[0])

