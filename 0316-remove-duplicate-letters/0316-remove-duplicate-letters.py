class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        counter = Counter(s)
        added = set()
        stack = []
        
        for char in s:
            if char in added:
                counter[char] -= 1
                continue
                
            while stack and stack[-1] > char and counter[stack[-1]] > 0:
                removed = stack.pop()
                added.remove(removed)
                
            stack.append(char)
            added.add(char)
            counter[char] -= 1
        
        return ''.join(stack)