class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        stack = []
        ma = 0
        for price in prices:
            while stack and stack[-1] > price:
                stack.pop()
            if stack:
                ma = max(ma,price - stack[-1])
            else:
                stack.append(price)
        return ma
            
        