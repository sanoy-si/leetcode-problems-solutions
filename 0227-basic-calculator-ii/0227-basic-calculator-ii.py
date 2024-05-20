class Solution:
    def calculate(self, s: str) -> int:
        new_s = []
        p = 0

        while p < len(s):
            curr = []
            while p < len(s) and s[p] in '0123456789':
                curr.append(s[p])
                p += 1

            if curr:
                new_s.append(''.join(curr))
            
            if p < len(s) and s[p] != ' ':
                new_s.append(s[p])
            
            p += 1
            
        stack = []

        for char in new_s:
            if stack and stack[-1] == '*':
                stack.pop()
                stack.append(str(int(stack.pop()) * int(char)))
            
            elif stack and stack[-1] == '/':
                stack.pop()
                val = int(stack.pop()) / int(char)
                stack.append(str(floor(val)) if val > 0 else str(ceil(val)))

            else:
                stack.append(char)

        print(stack)
        while len(stack) >= 3:
            first = int(stack.pop())
            
            if stack.pop() == '+':
                stack.append(str(int(stack.pop()) + first))
            
            else:
                stack.append(str(-int(stack.pop()) + first))
    
        return int(''.join(stack))