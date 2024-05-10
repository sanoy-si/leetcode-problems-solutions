class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        memory = {}
        n = len(prices)

        def dp(idx, bought):
            if idx >= n:
                return 0
            
            if (idx, bought) not in memory:
                if bought:
                    memory[(idx, bought)] = max(dp(idx + 1, False) + (prices[idx] - bought - fee), dp(idx + 1, bought))
                
                else:
                    memory[(idx, bought)] = max(dp(idx + 1, prices[idx]), dp(idx + 1, False))
                
            return memory[(idx, bought)]
        
        return dp(0, False)
            
