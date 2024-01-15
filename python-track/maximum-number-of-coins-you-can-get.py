class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        my_coins = 0
        p = 0
        
        while p < len(piles):
            piles.pop()
            my_coins += piles.pop()
            p += 1

        return my_coins
        