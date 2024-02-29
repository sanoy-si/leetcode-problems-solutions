class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        for char in s:
            if stack and char == ')':
                num = 0
                while stack and str(stack[-1]) not in '()':
                    num += int(stack.pop())
                stack.pop()

                if num == 0:
                    stack.append(1)

                else:
                    stack.append(2 * num)

            else:
                stack.append(char)
        
        return sum(stack)