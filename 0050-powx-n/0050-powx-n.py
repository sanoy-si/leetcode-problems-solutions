class Solution:
    def myPow(self, x: float, n: int) -> float:
        answer = 1
        n_was_negative = n < 0
        n = abs(n)
        while n:
            if n & 1:
                if n_was_negative:
                    answer /= x
                
                else:
                    answer *= x
            
            x *= x
            n >>= 1
        
        return answer
