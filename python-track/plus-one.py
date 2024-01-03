class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = [str(i) for i in digits]
        digits = int(''.join(digits)) + 1
        
        return [int(i) for i in str(digits)]
        
        
        
        