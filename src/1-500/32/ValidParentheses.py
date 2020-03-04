class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [0]
        ret = 0
        for char in s:
            if char == "(":
                stack.append(0)
            elif len(stack) > 1:
                stack[-2] += 2 + stack[-1]
                stack.pop()
                if ret < stack[-1]:
                    ret = stack[-1]
            else:
                stack[0] = 0
        return ret
