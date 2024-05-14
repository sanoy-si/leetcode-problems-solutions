class Solution:
    def integerBreak(self, n: int) -> int:
        memory = {}
        def dp(n, must):
            if n == 1:
                return 1 if not must else -inf
            
            if (n, must) not in memory:
                curr = 0
                for i in range(1, n):
                    curr = max(curr, i * dp(n - i, False))
                
                if not must:
                    curr = max(curr, n)
                
                memory[(n, must)] = curr
            
            return memory[(n, must)]
        
        return dp(n, True)
