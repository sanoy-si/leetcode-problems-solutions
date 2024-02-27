class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []

        for n in num:
            while k and stack and int(stack[-1]) > int(n):
                stack.pop()
                k -= 1
            stack.append(n)
        
        while stack and k:
            stack.pop()
            k -= 1

        p = 0
        while p < len(stack) and stack[p] == '0':
            p += 1

        stack = stack[p:]

        return ''.join(stack) if stack else '0'