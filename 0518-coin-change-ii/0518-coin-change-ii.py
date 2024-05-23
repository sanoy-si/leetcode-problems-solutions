class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [[0 for _ in range(amount + 1)] for _ in range(len(coins) + 1)]
        dp[-1] = [0 for _ in range(amount + 1)]

        for i in range(len(coins)):
            dp[i][-1] = 1

        for i in range(len(coins) - 1, -1, -1):
            for j in range(amount - 1, -1, -1):
                dp[i][j] = dp[i + 1][j]
                
                if j + coins[i] <= amount:
                    dp[i][j] += dp[i][j + coins[i]] 
        
        return dp[0][0]
                


        
            
                    