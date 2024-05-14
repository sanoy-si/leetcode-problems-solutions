class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memory = {}
        def dp(amount, idx):
            if amount == 0:
                return 1
            
            if amount < 0:
                return 0
            
            if (amount, idx) not in memory:
                memory[(amount, idx)] = 0
                for i in range(idx, len(coins)):
                    memory[(amount, idx)] += dp(amount - coins[i], i)
                
            return memory[(amount, idx)]
        
        return dp(amount, 0)

            
                    