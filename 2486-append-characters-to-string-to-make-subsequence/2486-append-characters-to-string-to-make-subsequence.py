class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        t_pointer = s_pointer = 0
        while t_pointer < len(t):
            while s_pointer < len(s) and s[s_pointer] != t[t_pointer]:
                s_pointer += 1
            
            if s_pointer < len(s) and s[s_pointer] == t[t_pointer]:
                t_pointer += 1
                s_pointer += 1
            
            else:
                break
            
        return len(t) - t_pointer 
            