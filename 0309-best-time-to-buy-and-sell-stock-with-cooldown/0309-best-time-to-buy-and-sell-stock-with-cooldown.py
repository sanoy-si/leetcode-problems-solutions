class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memory = {}
        
        def dp(idx, bought):
            if idx >= len(prices):
                return 0
            
            if (idx, bought) not in memory:
                if bought:
                    sell = prices[idx] + dp(idx + 2, False)
                    dont_sell = dp(idx + 1, bought)
                    memory[(idx, bought)] = max(sell, dont_sell)
                
                else:
                    buy = dp(idx + 1, True) - prices[idx]
                    dont_buy = dp(idx + 1, False)
                    memory[(idx, bought)] = max(buy, dont_buy)
                
            return memory[(idx, bought)]

        return dp(0, False)