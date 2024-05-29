class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n & (n - 1):
            return False
        
        for i in range(32):
            if n & 1 << i:
                return i % 2 == 0 
        
        return False