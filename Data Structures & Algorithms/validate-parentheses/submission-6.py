class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1:
            return False
        stack = []
        for char in s:
            if char == '(' or char == '{' or char == '[':
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False
                open = stack.pop()
                print(open)
                if open == '(' and char != ')':
                    return False
                elif open == '{' and char != '}':
                    return False
                elif open == '[' and char != ']':
                    return False
        return len(stack) == 0
            