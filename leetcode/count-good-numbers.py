class Solution:
    def countGoodNumbers(self, n: int) -> int:
        
        MOD = int(1e9 + 7)

        def pow(x, n):
                
            if n == 0:
                return 1
                
            if n == 1:
                return x
            
            temp = pow(x, n//2) % MOD

            if n % 2 == 0:
                return (temp * temp) % MOD

            return (temp * temp * x) % MOD


        half = n // 2 
        
        if n % 2 == 0:
            return int((pow(5, half) * pow(4, half)) % MOD)

        return int((pow(5, half + 1) * pow(4, half)) % MOD)