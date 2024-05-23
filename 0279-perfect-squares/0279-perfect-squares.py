class Solution:
    def numSquares(self, n: int) -> int:
        perfect_squares = []
        for i in range(1, n + 1):
            sqrt_ = sqrt(i)
            if sqrt_ == int(sqrt_):
                perfect_squares.append(i)
                
        memo = {}
        def dp(n):
            if n == 0:
                return 0
            
            if n not in memo:
                curr = inf
                for num in perfect_squares:
                    if n - num >= 0:
                        curr = min(curr, dp(n - num))
                
                memo[n] = 1 + curr
            
            return memo[n]
        
        return dp(n)


            
            