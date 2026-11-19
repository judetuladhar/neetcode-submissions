class Solution:
    def isValid(self, s: str) -> bool:
        chars = list(s)
        stack = []
        empty_list = []

        for c in chars:
            match c:
                case ')':
                    if stack == empty_list: return False
                    if '(' == stack[-1]:
                        stack.pop()
                    else:
                        return False
                case '}':
                    if stack == empty_list: return False
                    if '{' == stack[-1]:
                        stack.pop()
                    else:
                        return False
                case ']':
                    if stack == empty_list: return False
                    if '[' == stack[-1]:
                        stack.pop()
                    else:
                        return False
                case _:
                    stack.append(c)
        if stack == empty_list:
            return True
        return False
            