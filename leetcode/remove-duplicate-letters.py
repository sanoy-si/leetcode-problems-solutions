class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        counter = Counter(s)
        s_set = set()
        stack = []

        for char in s:
            if char in s_set:
                counter [char] -= 1
                continue
            
            while stack and stack[-1] > char and counter[stack[-1]] > 1:
                top_char = stack.pop()
                counter[top_char] -= 1
                s_set.remove(top_char)
            
            stack.append(char)
            s_set.add(char)
        
        return ''.join(stack)
