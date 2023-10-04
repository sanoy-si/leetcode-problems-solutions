class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        left = 0
        right = len(piles) - 1
        mine = 0
        
        for i in range((right + 1)//3):
            
            left += 1
            right -= 1
            mine += piles[right]
            right -= 1
        
        return mine
            
        