class Solution:
    def minSteps(self, n: int) -> int:
        memo = [[None for _ in range(n + 1)] for _ in range(n + 1)]

        def dp(num, copied_num):
            if num == n:
                return 0
            
            if memo[num][copied_num] == -1:
                return inf
            
            if memo[num][copied_num] == None:
                copy_ = inf
                paste = inf
                memo[num][copied_num] = -1

                if num != copied_num:
                    copy_ = 1 + dp(num, num)
                
                if num + copied_num <= n:
                    paste = 1 + dp(num + copied_num, copied_num)
               
                memo[num][copied_num] = min(copy_, paste)
            
            return memo[num][copied_num]
        
        return dp(1, 0)