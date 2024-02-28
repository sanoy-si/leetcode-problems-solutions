class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            n = abs(n)
            x = 1 / x
            
        if n == 0:
            return 1

        if n == 1:
            return x
        
        temp = self.myPow(x, n // 2)

        if n % 2 == 0:
            return temp * temp 

        return temp * temp * x
