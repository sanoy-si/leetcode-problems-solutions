class Solution:
    def divide(self, s):
        if len(s) == 1:return s
        mid = len(s)//2
        left = self.divide(s[0:mid])
        right = self.divide(s[mid:])
        return right + left

    def reverseString(self, s: List[str]) -> None:
        for i,j in enumerate(self.divide(s)):s[i] = j
        
        
    
    
            
        