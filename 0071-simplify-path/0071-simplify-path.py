class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for char in path:
            if char == '/':
                if stack and stack[-1] == '/':
                    continue
                elif len(stack) >= 3 and stack[-3] == '/' and stack [-2] == stack[-1] == '.':
                    for i in range(3):
                        stack.pop()
                    while stack and stack[-1] != '/':
                        stack.pop()
                    if not stack: 
                        stack.append('/')
                    
                elif len(stack) >= 2 and stack[-2] == '/' and stack[-1] == '.':
                        stack.pop()
                else:
                    stack.append('/')
            else:
                stack.append(char)
            
        

        if len(stack) >= 3 and stack[-3] == '/' and stack [-2] == stack[-1] == '.':
            for i in range(3):
                stack.pop()
            while stack and stack[-1] != '/':
                stack.pop()
            if not stack: 
                stack.append('/')
                    
        elif len(stack) >= 2 and stack[-2] == '/' and stack[-1] == '.':
                stack.pop()
        if stack and stack[-1] == '/' and len(stack) != 1:
            stack.pop()
        return ''.join(stack)
             

        