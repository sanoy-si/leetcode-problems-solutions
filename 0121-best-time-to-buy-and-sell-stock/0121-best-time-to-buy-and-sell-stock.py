class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        answer = 0
        smallest_price = inf

        for price in prices:
            answer = max(answer, price - smallest_price)
            smallest_price = min(smallest_price, price)
        
        return answer