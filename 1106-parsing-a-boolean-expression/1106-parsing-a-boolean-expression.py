class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        stack = []
        for char in expression:
            if char == ',':
                continue
            
            if char == ')':
                arr = []
                while stack and stack[-1] != '(':
                    arr.append(stack.pop())
                
                stack.pop()
                operation = stack.pop()
                if operation == "&":
                    stack.append(all(arr))
                
                elif operation == '|':
                    stack.append(any(arr))
                
                else:
                    stack.append(not all(arr))
            
            else:
                if char in "(|!&":
                    stack.append(char)
                
                else:
                    stack.append(True if char == "t" else False)

        return stack[-1]