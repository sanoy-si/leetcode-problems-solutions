class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n < 4:
            return n == 1
        
        return self.isPowerOfFour(n / 4)