class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if not stack:
                stack.append(c)
            else:
                if c in ['(', '[', '{']:
                    stack.append(c)
                else:
                    top = stack.pop()
                    if (top == '(' and c != ')') or \
                            (top == '[' and c != ']') or \
                            (top == '{' and c != '}'):
                        return False
        return not stack


solution = Solution()
print(solution.isValid("()[]{}"))