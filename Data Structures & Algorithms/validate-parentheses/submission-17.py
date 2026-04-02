class Solution:
    def isValid(self, s: str) -> bool:
        bracket_mapping = {"(": ")", "{": "}", "[": "]"}

        stack = []

        # iterate list: O(n)
        for c in s:
            if c in bracket_mapping:
                # appending is O(1) amortized
                stack.append(c)
            else:
                # popping is O(1)
                # note removing from beginning is O(n) as all elements need to be shifted left
                if len(stack) != 0 and bracket_mapping[stack[-1]] == c:
                    stack.pop()
                else:
                    return False
        
        return len(stack) == 0