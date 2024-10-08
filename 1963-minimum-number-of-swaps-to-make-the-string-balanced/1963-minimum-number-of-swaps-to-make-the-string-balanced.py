class Solution:
    def minSwaps(self, s: str) -> int:
        stack = []
        for char in s:
            # print(stack)
            if char == "]":
                if stack and stack[-1] == "[":
                    stack.pop()
                    continue
                
                else:
                    stack.append(char)
            
            else:
                stack.append(char)
        
        if not stack:
            return 0

        opened = len(stack) - 1
        closed = stack.index(']')
        while opened >= 0 and stack[opened] == ']':
            opened -= 1
        
        count = 0
        while opened > closed:
            count += 1
            stack[opened], stack[closed] = stack[closed], stack[opened]
            
            while opened >= 0 and stack[opened] == ']':
                opened -= 1
            
            while closed < len(stack) and stack[closed] == '[':
                closed += 1
        
        return max(1, count - 1)



