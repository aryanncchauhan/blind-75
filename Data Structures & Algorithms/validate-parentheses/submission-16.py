class Solution:
    def isValid(self, s: str) -> bool:
        bracket_mapping = {"(": ")", "{": "}", "[": "]"}

        stack = []

        for c in s:
            if c in bracket_mapping:
                stack.append(c)
            else:
                if len(stack) != 0 and bracket_mapping[stack[-1]] == c:
                    stack.pop()
                else:
                    return False
        
        return len(stack) == 0