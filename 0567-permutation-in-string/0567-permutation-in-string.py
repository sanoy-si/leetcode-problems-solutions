class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        mc = Counter(s1)
        c = {}
        if len(s1) > len(s2):return False
        for i in range(len(s1)):
            val = c.get(s2[i],0)
            c[s2[i]] = val + 1
        
        if c == mc:return True
        
        left = 0
        right = len(s1)
        
        while right < len(s2):
            if c[s2[left]] == 1:
                c.pop(s2[left])
            else:
                c[s2[left]] -= 1
            
            val = c.get(s2[right],0)
            c[s2[right]] = val + 1

            left += 1
            right += 1

            
            if c== mc:return True
        
        
        return False
                