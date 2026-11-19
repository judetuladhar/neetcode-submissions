class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for c in s:
            match c:
                case ')':
                    if not stack: return False
                    if '(' == stack[-1]:
                        stack.pop()
                    else:
                        return False
                case '}':
                    if not stack: return False
                    if '{' == stack[-1]:
                        stack.pop()
                    else:
                        return False
                case ']':
                    if not stack: return False
                    if '[' == stack[-1]:
                        stack.pop()
                    else:
                        return False
                case _:
                    stack.append(c)
        if not stack:
            return True
        return False
            