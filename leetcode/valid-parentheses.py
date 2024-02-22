class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if stack and ((stack[-1] == '(' and char == ')') or (stack[-1] == '{' and char == '}') or (stack[-1] == '[' and char == ']')):
                stack.pop()
            else:
                stack.append(char)
        
        return not stack