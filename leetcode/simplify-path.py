class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        path = list(path)
        path.append('/')
        
        for char in path:
            if char == '/':
                if stack and stack[-1] == '/':
                    continue

                cmd = []
                while len(stack) > 1 and stack[-1] != '/':
                    cmd.append(stack.pop())
                
                if not cmd:
                    stack.append('/')
                    
                elif cmd == ['.','.']:
                    stack.pop()
                    while len(stack) > 1 and stack[-1] != '/':
                        stack.pop()

                    if not stack:
                        stack.append('/')

                elif cmd != ['.']:
                    stack.append(''.join(reversed(cmd)))
                    stack.append('/')
            else:
                stack.append(char)

        if len(stack) > 1 and stack[-1] == '/':
            stack.pop()

        return ''.join(stack)

